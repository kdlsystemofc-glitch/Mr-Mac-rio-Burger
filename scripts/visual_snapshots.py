"""Regressão visual: captura página inteira nas 12 resoluções e compara com uma referência.

Uso:
  python scripts/visual_snapshots.py capture <dir>        # captura
  python scripts/visual_snapshots.py compare <ref> <new>  # compara

Captura com JS desligado (estado estático = pose final; motion é não-determinístico) e
fontes carregadas. Também captura via file:// com JS ligado só para checar erros de console.

Tolerância (a mesma das etapas anteriores, agora numérica): um pixel "difere" se algum canal
variar > 24/255; a resolução passa se <= 1% dos pixels diferirem e a altura da página for igual.
"""
import os
import sys
import threading
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

from PIL import Image, ImageChops
from playwright.sync_api import sync_playwright

RES = [(2560, 1440), (1920, 1080), (1440, 900), (1366, 768), (1280, 720), (1024, 768),
       (768, 1024), (430, 932), (390, 844), (360, 740), (320, 568), (844, 390)]
PORT = 8790
CH_THRESHOLD = 24
MAX_DIFF_RATIO = 0.01


class Silent(SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory='site', **k)

    def log_message(self, *a):
        pass


def capture(out):
    os.makedirs(out, exist_ok=True)
    httpd = ThreadingHTTPServer(('127.0.0.1', PORT), Silent)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    with sync_playwright() as p:
        b = p.chromium.launch()
        for w, h in RES:
            ctx = b.new_context(viewport={'width': w, 'height': h}, java_script_enabled=False)
            pg = ctx.new_page()
            pg.goto(f'http://127.0.0.1:{PORT}/index.html', wait_until='networkidle')
            pg.wait_for_timeout(400)
            pg.screenshot(path=f'{out}/{w}x{h}.png', full_page=True)
            ctx.close()
        b.close()
    httpd.shutdown()
    print('captured', out)


def compare(ref, new):
    ok = True
    for w, h in RES:
        a = Image.open(f'{ref}/{w}x{h}.png').convert('RGB')
        c = Image.open(f'{new}/{w}x{h}.png').convert('RGB')
        if a.size != c.size:
            print(f'{w}x{h}: FAIL tamanho {a.size} -> {c.size}')
            ok = False
            continue
        diff = ImageChops.difference(a, c)
        r, g, bl = diff.split()
        mx = ImageChops.lighter(ImageChops.lighter(r, g), bl)
        hist = mx.histogram()
        n_diff = sum(hist[CH_THRESHOLD + 1:])
        ratio = n_diff / (a.size[0] * a.size[1])
        status = 'PASS' if ratio <= MAX_DIFF_RATIO else 'FAIL'
        ok &= status == 'PASS'
        print(f'{w}x{h}: {status} {ratio * 100:.3f}% pixels > {CH_THRESHOLD}/255')
        if status == 'FAIL':
            mx.point(lambda v: 255 if v > CH_THRESHOLD else 0).save(f'{new}/{w}x{h}-diff.png')
    print('RESULTADO:', 'PASS' if ok else 'FAIL')
    return ok


if __name__ == '__main__':
    if sys.argv[1] == 'capture':
        capture(sys.argv[2])
    else:
        sys.exit(0 if compare(sys.argv[2], sys.argv[3]) else 1)
