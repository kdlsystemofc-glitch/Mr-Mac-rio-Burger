import asyncio
from playwright.async_api import async_playwright
import os

async def test_hero():
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

        # Disparar interação para carregar scripts imediatamente se não carregou
        await page.mouse.move(500, 300)
        await page.wait_for_timeout(2000)

        # 1. Verificar execução do Hero Motion
        hero_status = await page.evaluate("""() => {
            const burger = document.querySelector('.hero-burger-img');
            const bgText = document.querySelector('.hero-bg-text');
            const fries = document.querySelector('.fries-fly-wrapper img');
            return {
                hasSections: typeof window.MrMacarioSections !== 'undefined',
                hasHeroInit: typeof window.MrMacarioSections.initHero !== 'undefined',
                burgerVisible: burger ? window.getComputedStyle(burger).opacity : null,
                bgTextVisible: bgText ? window.getComputedStyle(bgText).opacity : null,
                friesVisible: fries ? window.getComputedStyle(fries).opacity : null,
                activeLoops: window.MrMacarioMotion ? window.MrMacarioMotion.activeLoops.length : 0
            };
        }""")
        print("Status do Hero Motion:", hero_status)
        assert hero_status['hasSections'], "MrMacarioSections não definido"
        assert float(hero_status['burgerVisible']) >= 0.9, "Burger invisível após animação"
        assert hero_status['activeLoops'] >= 2, "Loops contínuos do Hero não registrados"

        # 2. Capturar Screenshot do Hero assentado
        hero_elem = page.locator("#hero")
        os.makedirs("screenshots/motion", exist_ok=True)
        await hero_elem.screenshot(path="screenshots/motion/hero_settled.png")
        print("Screenshot do Hero salvo em screenshots/motion/hero_settled.png")

        # 3. Teste de Scroll rápido / nada preso
        await page.evaluate("window.scrollTo(0, 1000)")
        await page.wait_for_timeout(300)
        await page.evaluate("window.scrollTo(0, 0)")
        await page.wait_for_timeout(500)

        burger_opacity = await page.evaluate("() => window.getComputedStyle(document.querySelector('.hero-burger-img')).opacity")
        assert float(burger_opacity) >= 0.9, "Elemento ficou preso após scroll rápido!"

        # 4. Verificar erros no console
        print("Erros no console:", console_errors)
        assert len(console_errors) == 0, f"Erros encontrados: {console_errors}"

        print("=== TESTE HERO MOTION PASSOU COM SUCESSO! ===")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_hero())
