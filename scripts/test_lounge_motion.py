import asyncio
from playwright.async_api import async_playwright
import os

async def test_lounge():
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

        # Rolar até a seção do lounge
        await page.locator("#lounge-social").scroll_into_view_if_needed()
        await page.wait_for_timeout(1800)

        # 1. Verificar execução do Lounge Motion
        lounge_status = await page.evaluate("""() => {
            const title = document.querySelector('.lounge-title');
            const trophy = document.querySelector('.trophy-img');
            const photoL = document.querySelector('.lounge-photo-left .photo-frame');
            const photoR = document.querySelector('.lounge-photo-right .photo-frame');
            const badge = document.querySelector('.badge-google-reviews');
            const tape = document.querySelector('.tape-strip');

            return {
                titleVisible: title ? window.getComputedStyle(title).opacity : null,
                trophyVisible: trophy ? window.getComputedStyle(trophy).opacity : null,
                photoLVisible: photoL ? window.getComputedStyle(photoL).opacity : null,
                photoRVisible: photoR ? window.getComputedStyle(photoR).opacity : null,
                badgeVisible: badge ? window.getComputedStyle(badge).opacity : null,
                tapeVisible: tape ? window.getComputedStyle(tape).opacity : null,
                activeLoops: window.MrMacarioMotion ? window.MrMacarioMotion.activeLoops.length : 0
            };
        }""")
        print("Status do Lounge Motion:", lounge_status)
        assert float(lounge_status['titleVisible']) >= 0.9, "Título do Lounge não visível"
        assert float(lounge_status['trophyVisible']) >= 0.9, "Troféu não visível"
        assert float(lounge_status['photoLVisible']) >= 0.9, "Foto esquerda não visível"
        assert float(lounge_status['photoRVisible']) >= 0.9, "Foto direita não visível"
        assert float(lounge_status['badgeVisible']) >= 0.9, "Selo Google não visível"
        assert float(lounge_status['tapeVisible']) >= 0.9, "Fita crepe não visível"

        # 2. Capturar Screenshot do Lounge assentado
        lounge_elem = page.locator("#lounge-social")
        os.makedirs("screenshots/motion", exist_ok=True)
        await lounge_elem.screenshot(path="screenshots/motion/lounge_settled.png")
        print("Screenshot do Lounge salvo em screenshots/motion/lounge_settled.png")

        # 3. Teste de Scroll rápido
        await page.evaluate("window.scrollTo(0, 3500)")
        await page.wait_for_timeout(300)
        await page.locator("#lounge-social").scroll_into_view_if_needed()
        await page.wait_for_timeout(500)

        trophy_opacity = await page.evaluate("() => window.getComputedStyle(document.querySelector('.trophy-img')).opacity")
        assert float(trophy_opacity) >= 0.9, "Troféu ficou preso após scroll rápido!"

        # 4. Verificar erros no console
        print("Erros no console:", console_errors)
        assert len(console_errors) == 0, f"Erros encontrados: {console_errors}"

        print("=== TESTE LOUNGE MOTION PASSOU COM SUCESSO! ===")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_lounge())
