import asyncio
from playwright.async_api import async_playwright
import os

async def test_menu():
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

        # Rolar suavemente até a seção do menu
        await page.locator("#menu-highlights").scroll_into_view_if_needed()
        await page.wait_for_timeout(1800)

        # 1. Verificar execução do Menu Motion
        menu_status = await page.evaluate("""() => {
            const title = document.querySelector('.menu-title');
            const burguinho = document.querySelector('.item-burguinho .menu-food-visual');
            const fries = document.querySelector('.item-fries .menu-food-visual');
            const sandShape = document.querySelector('.menu-sand-shape');
            const sandStyle = window.getComputedStyle(sandShape);

            return {
                titleVisible: title ? window.getComputedStyle(title).opacity : null,
                burguinhoVisible: burguinho ? window.getComputedStyle(burguinho).opacity : null,
                friesVisible: fries ? window.getComputedStyle(fries).opacity : null,
                sandTransform: sandStyle.transform,
                activeLoops: window.MrMacarioMotion ? window.MrMacarioMotion.activeLoops.length : 0
            };
        }""")
        print("Status do Menu Motion:", menu_status)
        assert float(menu_status['titleVisible']) >= 0.9, "Título do menu não visível"
        assert float(menu_status['burguinhoVisible']) >= 0.9, "Burguinho não visível"
        assert float(menu_status['friesVisible']) >= 0.9, "Batatas não visíveis"
        assert menu_status['sandTransform'] == 'none', "Elemento contínuo (.menu-sand-shape) não pode ter transform!"

        # 2. Capturar Screenshot do Menu assentado
        menu_elem = page.locator("#menu-highlights")
        os.makedirs("screenshots/motion", exist_ok=True)
        await menu_elem.screenshot(path="screenshots/motion/menu_settled.png")
        print("Screenshot do Menu salvo em screenshots/motion/menu_settled.png")

        # 3. Teste de Scroll rápido
        await page.evaluate("window.scrollTo(0, 2000)")
        await page.wait_for_timeout(300)
        await page.locator("#menu-highlights").scroll_into_view_if_needed()
        await page.wait_for_timeout(500)

        burguinho_opacity = await page.evaluate("() => window.getComputedStyle(document.querySelector('.item-burguinho .menu-food-visual')).opacity")
        assert float(burguinho_opacity) >= 0.9, "Burguinho ficou preso após scroll rápido!"

        # 4. Verificar erros no console
        print("Erros no console:", console_errors)
        assert len(console_errors) == 0, f"Erros encontrados: {console_errors}"

        print("=== TESTE MENU MOTION PASSOU COM SUCESSO! ===")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_menu())
