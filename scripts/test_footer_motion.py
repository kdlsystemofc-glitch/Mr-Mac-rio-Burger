import asyncio
from playwright.async_api import async_playwright
import os

async def test_footer():
    site_path = os.path.abspath("site/index.html")
    url = f"file:///{site_path.replace(os.sep, '/')}"

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={"width": 1440, "height": 900})
        page = await context.new_page()

        console_errors = []
        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)

        print(f"Abrindo {url}...")
        await page.goto(url, wait_until="networkidle")

        # Rolar até o rodapé
        await page.locator("#footer-conversion").scroll_into_view_if_needed()
        await page.wait_for_timeout(1800)

        # 1. Verificar execução do Footer Motion
        footer_status = await page.evaluate("""() => {
            const title = document.querySelector('.footer-title');
            const btnCall = document.querySelector('.btn-call');
            const btnWa = document.querySelector('.btn-whatsapp');
            const hours = document.querySelector('.footer-hours-pill');
            const divider = document.querySelector('.film-strip-divider');

            return {
                titleVisible: title ? window.getComputedStyle(title).opacity : null,
                btnCallVisible: btnCall ? window.getComputedStyle(btnCall).opacity : null,
                btnWaVisible: btnWa ? window.getComputedStyle(btnWa).opacity : null,
                hoursVisible: hours ? window.getComputedStyle(hours).opacity : null,
                dividerTransform: window.getComputedStyle(divider).transform,
                activeLoops: window.MrMacarioMotion ? window.MrMacarioMotion.activeLoops.length : 0
            };
        }""")
        print("Status do Footer Motion:", footer_status)
        assert float(footer_status['titleVisible']) >= 0.9, "Título do rodapé não visível"
        assert float(footer_status['btnCallVisible']) >= 0.9, "Botão ligar não visível"
        assert float(footer_status['btnWaVisible']) >= 0.9, "Botão WhatsApp não visível"
        assert float(footer_status['hoursVisible']) >= 0.9, "Pílula de horários não visível"
        assert footer_status['dividerTransform'] == 'none', "Divisória de filme (.film-strip-divider) não pode ter transform!"

        # 2. Capturar Screenshot do Rodapé assentado
        footer_elem = page.locator("#footer-conversion")
        os.makedirs("screenshots/motion", exist_ok=True)
        await footer_elem.screenshot(path="screenshots/motion/footer_settled.png")
        print("Screenshot do Rodapé salvo em screenshots/motion/footer_settled.png")

        # 3. Teste de Scroll rápido
        await page.evaluate("window.scrollTo(0, 0)")
        await page.wait_for_timeout(300)
        await page.locator("#footer-conversion").scroll_into_view_if_needed()
        await page.wait_for_timeout(500)

        btn_opacity = await page.evaluate("() => window.getComputedStyle(document.querySelector('.btn-whatsapp')).opacity")
        assert float(btn_opacity) >= 0.9, "Botão do rodapé ficou preso após scroll rápido!"

        # 4. Verificar erros no console
        print("Erros no console:", console_errors)
        assert len(console_errors) == 0, f"Erros encontrados: {console_errors}"

        print("=== TESTE FOOTER MOTION PASSOU COM SUCESSO! ===")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_footer())
