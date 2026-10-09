import asyncio
from playwright.async_api import async_playwright
import os

async def test_griddle():
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

        # Rolar até a seção da chapa
        await page.locator("#griddle-craft").scroll_into_view_if_needed()
        await page.wait_for_timeout(1800)

        # 1. Verificar execução do Griddle Motion
        griddle_status = await page.evaluate("""() => {
            const title = document.querySelector('.griddle-title');
            const stamp = document.querySelector('.stamp-maillard');
            const arrow = document.querySelector('.chalk-arrow');
            const tornTop = document.querySelector('.torn-paper-top');
            const tornBottom = document.querySelector('.torn-paper-bottom');

            return {
                titleVisible: title ? window.getComputedStyle(title).opacity : null,
                stampVisible: stamp ? window.getComputedStyle(stamp).opacity : null,
                arrowVisible: arrow ? window.getComputedStyle(arrow).opacity : null,
                tornTopTransform: window.getComputedStyle(tornTop).transform,
                tornBottomTransform: window.getComputedStyle(tornBottom).transform,
                activeLoops: window.MrMacarioMotion ? window.MrMacarioMotion.activeLoops.length : 0
            };
        }""")
        print("Status do Griddle Motion:", griddle_status)
        assert float(griddle_status['titleVisible']) >= 0.9, "Título da chapa não visível"
        assert float(griddle_status['stampVisible']) >= 0.9, "Selo Maillard não visível"
        assert float(griddle_status['arrowVisible']) >= 0.9, "Seta de giz não visível"
        assert griddle_status['tornTopTransform'] == 'none', "Borda superior contínua não pode ter transform!"
        assert griddle_status['tornBottomTransform'] == 'none', "Borda inferior contínua não pode ter transform!"

        # 2. Capturar Screenshot da Chapa assentada
        griddle_elem = page.locator("#griddle-craft")
        os.makedirs("screenshots/motion", exist_ok=True)
        await griddle_elem.screenshot(path="screenshots/motion/griddle_settled.png")
        print("Screenshot da Chapa salvo em screenshots/motion/griddle_settled.png")

        # 3. Teste de Scroll rápido
        await page.evaluate("window.scrollTo(0, 3000)")
        await page.wait_for_timeout(300)
        await page.locator("#griddle-craft").scroll_into_view_if_needed()
        await page.wait_for_timeout(500)

        title_opacity = await page.evaluate("() => window.getComputedStyle(document.querySelector('.griddle-title')).opacity")
        assert float(title_opacity) >= 0.9, "Título da chapa ficou preso após scroll rápido!"

        # 4. Verificar erros no console
        print("Erros no console:", console_errors)
        assert len(console_errors) == 0, f"Erros encontrados: {console_errors}"

        print("=== TESTE GRIDDLE MOTION PASSOU COM SUCESSO! ===")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_griddle())
