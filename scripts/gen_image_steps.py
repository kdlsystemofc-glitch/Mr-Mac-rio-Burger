"""Gera degraus responsivos (srcset) a partir dos arquivos -1600.webp existentes.
(Testado derivar do -800: diferença de pixel maior que a partir do -1600.)

Só redimensiona (Lanczos) os arquivos reais já aprovados; não altera recorte nem cor.
Uso: python scripts/gen_image_steps.py
"""
import os
from PIL import Image

A = 'site/assets'
STEPS = {
    'hero-burger': [480, 640, 720, 1200],
    'menu-burguinho': [480, 720, 1200],
    'menu-fries': [480, 720, 1200],
    'lounge-left': [480, 640, 1200],
    'lounge-right': [480, 640, 1200],
    'trophy-5': [480, 1200],
    'griddle-craft': [480, 1200],
    'footer-diner': [480, 1200],
    'dice': [160, 320],
    'neon-doodle': [120, 240],
}

for name, widths in STEPS.items():
    src = Image.open(f'{A}/{name}-1600.webp')
    src.load()
    for w in widths:
        h = round(src.height * w / src.width)
        out = f'{A}/{name}-{w}.webp'
        im = src.resize((w, h), Image.LANCZOS)
        kw = dict(quality=82, method=6)
        if im.mode == 'RGBA':
            kw['alpha_quality'] = 100
        im.save(out, 'WEBP', **kw)
        print(f'{out}: {w}x{h} {os.path.getsize(out) // 1024} KB')
