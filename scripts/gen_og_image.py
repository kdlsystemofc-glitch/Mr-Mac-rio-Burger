"""Gera a imagem de compartilhamento (Open Graph / Twitter) 1200x630 a partir da composição
aprovada do hero, renderizada pelo próprio site — nada novo é desenhado ou gerado por IA.

Ficam de fora só os elementos com texto pequeno demais para miniatura de rede social
(comandas, selos, pílulas e o "BURGER" miúdo do letreiro) e o header/botão de pausa. Sobram o letreiro grande, o hambúrguer
(arquivo já aprovado), batatas, dados e neon. Sem pessoas -> sem pendência de direito de imagem.

Uso: python scripts/gen_og_image.py   (depois de npm run build)
Saída: site/assets/og-image.jpg
"""
import io
import os

from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'site', 'assets', 'og-image.jpg')
W, H = 1200, 630
HIDE = ('.receipt, .hero-brand-line2, .stamp-blue, .stamp-mint, .stamp-coral, .badge-fresh-meat, .badge-pill,'
        ' .motion-pause-btn, .site-header { visibility: hidden !important; }')


def main():
    url = 'file:///' + os.path.join(ROOT, 'site', 'index.html').replace(os.sep, '/')
    with sync_playwright() as p:
        browser = p.chromium.launch()
        ctx = browser.new_context(viewport={'width': W, 'height': H}, device_scale_factor=2)
        # estado estático (pose final): sem os scripts de motion
        ctx.route('**/js/**', lambda route: route.abort())
        page = ctx.new_page()
        page.goto(url, wait_until='networkidle')
        page.add_style_tag(content=HIDE)
        page.evaluate('document.fonts.ready')
        page.wait_for_timeout(300)
        box = page.evaluate("""() => { const r = document.querySelector('#hero').getBoundingClientRect();
                                       return [r.top + scrollY, r.height]; }""")
        png = page.screenshot(full_page=True, clip={'x': 0, 'y': box[0], 'width': W, 'height': box[1]})
        browser.close()

    im = Image.open(io.BytesIO(png)).convert('RGB')
    # "cover" 1200x630: escala até cobrir os dois lados e recorta o excedente, centralizado
    scale = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
    left, top = (im.width - W) // 2, (im.height - H) // 2
    im = im.crop((left, top, left + W, top + H))
    im.save(OUT, 'JPEG', quality=86, optimize=True, progressive=True)
    print(f'{OUT}: {im.size} {os.path.getsize(OUT) // 1024} KB (hero {box[1]:.0f}px de altura)')


if __name__ == '__main__':
    main()
