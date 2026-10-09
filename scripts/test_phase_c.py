import asyncio
from playwright.async_api import async_playwright
import os
import json

async def run_phase_c():
    site_path = os.path.abspath("site/index.html")
    url = f"file:///{site_path.replace(os.sep, '/')}"
    video_dir = os.path.abspath("screenshots/video")
    os.makedirs(video_dir, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(
            viewport={"width": 1440, "height": 900},
            record_video_dir=video_dir,
            record_video_size={"width": 1440, "height": 900}
        )
        page = await context.new_page()

        print(f"Iniciando gravação e navegação em {url}...")
        await page.goto(url, wait_until="networkidle")

        # Acionar scripts
        await page.mouse.move(400, 300)
        await page.wait_for_timeout(1800)

        # 1. Medir loops simultâneos na Seção 1 (Hero)
        hero_loops = await page.evaluate("""() => {
            return window.MrMacarioMotion.activeLoops.filter(l => l.isVisible && !l.tween.paused()).length;
        }""")
        print(f"[Hero (Scroll 0px)] Loops ativos simultaneamente: {hero_loops}")

        # 2. Rolar para Seção 2 (Menu Highlights)
        await page.locator("#menu-highlights").scroll_into_view_if_needed()
        await page.wait_for_timeout(1500)
        menu_loops = await page.evaluate("""() => {
            return window.MrMacarioMotion.activeLoops.filter(l => l.isVisible && !l.tween.paused()).length;
        }""")
        print(f"[Menu Highlights] Loops ativos simultaneamente: {menu_loops}")

        # 3. Rolar para Seção 3 (Griddle Craft)
        await page.locator("#griddle-craft").scroll_into_view_if_needed()
        await page.wait_for_timeout(1500)
        griddle_loops = await page.evaluate("""() => {
            return window.MrMacarioMotion.activeLoops.filter(l => l.isVisible && !l.tween.paused()).length;
        }""")
        print(f"[Griddle Craft] Loops ativos simultaneamente: {griddle_loops}")

        # 4. Rolar para Seção 4 (Lounge & Games)
        await page.locator("#lounge-social").scroll_into_view_if_needed()
        await page.wait_for_timeout(1500)
        lounge_loops = await page.evaluate("""() => {
            return window.MrMacarioMotion.activeLoops.filter(l => l.isVisible && !l.tween.paused()).length;
        }""")
        print(f"[Board Game Lounge] Loops ativos simultaneamente: {lounge_loops}")

        # 5. Rolar para Seção 5 (Footer & Conversion)
        await page.locator("#footer-conversion").scroll_into_view_if_needed()
        await page.wait_for_timeout(1500)
        footer_loops = await page.evaluate("""() => {
            return window.MrMacarioMotion.activeLoops.filter(l => l.isVisible && !l.tween.paused()).length;
        }""")
        print(f"[Footer & Conversion] Loops ativos simultaneamente: {footer_loops}")

        # Rolar de volta suavemente para capturar o ritmo completo
        await page.evaluate("""async () => {
            for (let y = document.body.scrollHeight; y >= 0; y -= 120) {
                window.scrollTo(0, y);
                await new Promise(r => setTimeout(r, 40));
            }
        }""")
        await page.wait_for_timeout(1000)

        # Salvar dados de auditoria de loops
        loop_audit = {
            "hero_loops": hero_loops,
            "menu_loops": menu_loops,
            "griddle_loops": griddle_loops,
            "lounge_loops": lounge_loops,
            "footer_loops": footer_loops,
            "max_simultaneous": max(hero_loops, menu_loops, griddle_loops, lounge_loops, footer_loops)
        }

        with open("loop_audit.json", "w", encoding="utf-8") as f:
            json.dump(loop_audit, f, indent=2)

        video_path = await page.video.path()
        print(f"Vídeo da página inteira gravado com sucesso em: {video_path}")

        await page.close()
        await context.close()
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_phase_c())
