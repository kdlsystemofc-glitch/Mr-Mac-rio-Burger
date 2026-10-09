import asyncio
from playwright.async_api import async_playwright
import os

async def test_motion_base():
    site_path = os.path.abspath("site/index.html")
    url = f"file:///{site_path.replace(os.sep, '/')}"

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={"width": 1280, "height": 800})
        page = await context.new_page()

        console_errors = []
        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)

        print(f"Navegando para {url}...")
        await page.goto(url, wait_until="networkidle")

        # Aguardar os scripts diferidos de motion carregarem (timeout 2s)
        await page.wait_for_timeout(1500)

        # 1. Verificar se window.MrMacarioMotion foi inicializado
        motion_state = await page.evaluate("""() => {
            return {
                exists: typeof window.MrMacarioMotion !== 'undefined',
                mode: window.MrMacarioMotion ? window.MrMacarioMotion.mode : null,
                quality: window.MrMacarioMotion ? window.MrMacarioMotion.quality : null,
                hasGsap: typeof window.gsap !== 'undefined',
                hasScrollTrigger: typeof window.ScrollTrigger !== 'undefined',
                hasLenis: typeof window.Lenis !== 'undefined',
                htmlMode: document.documentElement.getAttribute('data-motion-mode'),
                htmlQuality: document.documentElement.getAttribute('data-motion-quality')
            };
        }""")
        print("Estado do Motion Core:", motion_state)
        assert motion_state['exists'], "MrMacarioMotion não encontrado no window"
        assert motion_state['hasGsap'], "GSAP não carregado"
        assert motion_state['hasScrollTrigger'], "ScrollTrigger não carregado"
        assert motion_state['hasLenis'], "Lenis não carregado"

        # 2. Testar o botão de pausa
        pause_btn = page.locator("#motion-pause-toggle")
        assert await pause_btn.is_visible(), "Botão de pausa não está visível"

        box = await pause_btn.bounding_box()
        assert box['width'] >= 44 and box['height'] >= 44, f"Alvo de toque inválido: {box['width']}x{box['height']}"

        # Clicar para pausar
        await pause_btn.click()
        await page.wait_for_timeout(200)

        is_paused = await page.evaluate("() => window.MrMacarioMotion.mode === 'paused' && window.MrMacarioMotion.isPausedByUser")
        print("Modo após clique no botão:", is_paused)
        assert is_paused, "Falha ao alternar para modo pausado"

        # Clicar para retomar
        await pause_btn.click()
        await page.wait_for_timeout(200)
        is_resumed = await page.evaluate("() => window.MrMacarioMotion.mode === 'full' && !window.MrMacarioMotion.isPausedByUser")
        print("Modo após segundo clique:", is_resumed)
        assert is_resumed, "Falha ao retomar do modo pausado"

        # 3. Testar se elementos decorativos contínuos estão intactos (sem transform/opacity em ancestrais)
        torn_elements = await page.evaluate("""() => {
            const el = document.querySelector('.torn-paper');
            if (!el) return { found: false };
            const style = window.getComputedStyle(el);
            return {
                found: true,
                transform: style.transform,
                opacity: style.opacity
            };
        }""")
        print("Verificação do elemento decorativo contínuo (.torn-paper):", torn_elements)
        assert torn_elements['transform'] == 'none', "Elemento contínuo não pode ter transform!"

        # 4. Verificar se há erros no console
        print("Erros no console:", console_errors)
        assert len(console_errors) == 0, f"Erros encontrados no console: {console_errors}"

        print("=== TESTE DA FASE A PASSOU COM SUCESSO! ===")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_motion_base())
