"""Gera favicons e ícones do manifest a partir do logo REAL do cliente (logo-macario-1600.webp,
selo oficial vindo de imagens/imgi_2). Só redimensiona; nada é redesenhado.

Uso: python scripts/gen_icons.py
Saídas em site/: favicon.ico (16/32/48), apple-touch-icon.png (180),
icons/icon-192.png, icons/icon-512.png, icons/icon-maskable-512.png
"""
import os

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, 'site')
SRC = os.path.join(ROOT, 'reserva', 'logo-macario-1600.webp')  # fora do deploy; só fonte dos ícones


def main():
    logo = Image.open(SRC).convert('RGB')
    bg = logo.getpixel((5, 5))  # cor do fundo creme do próprio arquivo do logo
    os.makedirs(os.path.join(SITE, 'icons'), exist_ok=True)

    def sized(n):
        return logo.resize((n, n), Image.LANCZOS)

    def save_png(im, path):
        # paleta de 256 cores: ~60% menor, diferença média ~1,7/255 (medido) — imperceptível em ícone
        pal = im.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.FLOYDSTEINBERG)
        pal.save(path, optimize=True)

    sized(256).save(os.path.join(SITE, 'favicon.ico'), sizes=[(16, 16), (32, 32), (48, 48)])
    save_png(sized(180), os.path.join(SITE, 'apple-touch-icon.png'))
    save_png(sized(192), os.path.join(SITE, 'icons', 'icon-192.png'))
    save_png(sized(512), os.path.join(SITE, 'icons', 'icon-512.png'))

    # maskable: o logo ocupa 80% (zona segura do Android), margem na cor de fundo do logo
    canvas = Image.new('RGB', (512, 512), bg)
    inner = sized(410)
    canvas.paste(inner, ((512 - 410) // 2, (512 - 410) // 2))
    save_png(canvas, os.path.join(SITE, 'icons', 'icon-maskable-512.png'))

    for f in ('favicon.ico', 'apple-touch-icon.png', 'icons/icon-192.png', 'icons/icon-512.png',
              'icons/icon-maskable-512.png'):
        print(f, os.path.getsize(os.path.join(SITE, f)) // 1024, 'KB')
    print('cor de fundo do logo:', '#%02x%02x%02x' % bg)


if __name__ == '__main__':
    main()
