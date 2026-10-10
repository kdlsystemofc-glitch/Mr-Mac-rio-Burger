"""Auditoria final: todas as telas × modos × motores (Chromium e WebKit).

Uso: python scripts/auditoria_final.py [saida_dir]
Gera <saida_dir>/relatorio.json, screenshots por motor/tela e imprime um resumo.

Modos:
  padrao   — HTTP, JS ligado, motion completo (aguarda o motion carregar e assentar)
  reduzido — prefers-reduced-motion: reduce
  escuro   — prefers-color-scheme: dark
  sem-js   — JavaScript desligado (progressive enhancement)
  arquivo  — file:// (só Chromium; WebKit no Windows não abre file:// de forma confiável)

Checagens por combinação: rolagem horizontal, erros de console/página, requisições com falha,
imagens quebradas, alvos de toque < 44px (telas <= 1024), um único <h1>, <img> sem alt,
seções de borda a borda (largura == viewport), e, com JS, se o motion iniciou/respeitou o modo.
"""
import json
import os
import sys
import threading
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, 'site')
PORT = 8796
RES = [(5120, 1440), (3840, 2160), (3440, 1440), (2560, 1440), (1920, 1080), (1440, 900), (1366, 768),
       (1280, 720), (1024, 768), (768, 1024), (430, 932), (390, 844), (360, 740), (320, 568), (844, 390)]
MOBILE_MAX = 1024


class Silent(SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=SITE, **k)

    def log_message(self, *a):
        pass


CHECK_JS = """(mobile) => {
  const doc = document.documentElement;
  const out = {};
  out.overflowX = Math.max(doc.scrollWidth - doc.clientWidth, document.body.scrollWidth - document.body.clientWidth);
  out.h1 = document.querySelectorAll('h1').length;
  out.imgSemAlt = [...document.images].filter(i => !i.hasAttribute('alt')).map(i => i.getAttribute('src'));
  out.imgQuebrada = [...document.images].filter(i => i.complete && i.naturalWidth === 0).map(i => i.getAttribute('src'));
  const vw = doc.clientWidth;
  out.secaoEstreita = [...document.querySelectorAll('main > section, main > footer, header.site-header')]
    .filter(s => Math.abs(s.getBoundingClientRect().width - vw) > 1).map(s => s.id || s.className);
  out.toque = [];
  if (mobile) {
    for (const el of document.querySelectorAll('a, button')) {
      const r = el.getBoundingClientRect(); const cs = getComputedStyle(el);
      if (cs.display === 'none' || cs.visibility === 'hidden' || r.width === 0) continue;
      if (r.width < 43.5 || r.height < 43.5) out.toque.push(`${el.textContent.trim().slice(0, 25)} ${Math.round(r.width)}x${Math.round(r.height)}`);
    }
  }
  out.motion = window.MrMacarioMotion ? { modo: doc.getAttribute('data-motion-mode'), qualidade: doc.getAttribute('data-motion-quality') } : null;
  // conteúdo visível com motion assentado: nada essencial deve ficar com opacidade 0
  out.invisiveis = [...document.querySelectorAll('h1, h2, .hero-burger-img, .menu-food-img, .neon-pill-btn, .footer-address')]
    .filter(e => parseFloat(getComputedStyle(e).opacity) < 0.5).map(e => e.className || e.tagName);
  return out;
}"""


def run_combo(browser, engine, mode, w, h, shots):
    opts = {'viewport': {'width': w, 'height': h}}
    if mode == 'reduzido':
        opts['reduced_motion'] = 'reduce'
    if mode == 'escuro':
        opts['color_scheme'] = 'dark'
    if mode == 'sem-js':
        opts['java_script_enabled'] = False
    if w <= 430 or (w == 844 and h == 390):
        opts.update(is_mobile=engine == 'chromium', has_touch=True)
    ctx = browser.new_context(**opts)
    page = ctx.new_page()
    erros, falhas = [], []
    page.on('console', lambda m: m.type == 'error' and erros.append(m.text[:160]))
    page.on('pageerror', lambda e: erros.append('EXC ' + str(e)[:160]))
    page.on('requestfailed', lambda r: falhas.append(r.url.split('/')[-1] + ' ' + (r.failure or '')))
    url = ('file:///' + os.path.join(SITE, 'index.html').replace(os.sep, '/')) if mode == 'arquivo' \
        else f'http://127.0.0.1:{PORT}/index.html'
    page.goto(url, wait_until='load')
    if mode != 'sem-js':
        page.mouse.move(w // 3, h // 3)  # primeira interação: dispara o carregamento do motion
        page.wait_for_function('() => !!window.MrMacarioMotion', timeout=10000)
        # rola até o fim e volta, para todas as seções revelarem e as imagens lazy carregarem
        total = page.evaluate('document.documentElement.scrollHeight')
        for y in range(0, total, max(300, h // 2)):
            page.evaluate(f'window.scrollTo(0, {y})')
            page.wait_for_timeout(120)
        page.wait_for_timeout(2500)
        page.evaluate('window.scrollTo(0, 0)')
        page.wait_for_timeout(1500)
    else:
        total = page.evaluate('document.documentElement.scrollHeight')
        for y in range(0, total, max(300, h // 2)):
            page.evaluate(f'window.scrollTo(0, {y})')
            page.wait_for_timeout(60)
        page.evaluate('window.scrollTo(0, 0)')
        page.wait_for_timeout(500)
    r = page.evaluate(CHECK_JS, w <= MOBILE_MAX)
    r['console'] = erros
    r['falhas'] = falhas
    if shots and mode in ('padrao', 'sem-js'):
        os.makedirs(shots, exist_ok=True)
        page.screenshot(path=os.path.join(shots, f'{engine}_{mode}_{w}x{h}.png'), full_page=True)
    ctx.close()
    return r


def problemas(r, mode):
    p = []
    if r['overflowX'] > 1:
        p.append(f"rolagem horizontal {r['overflowX']}px")
    if r['h1'] != 1:
        p.append(f"{r['h1']} h1")
    for k, label in (('imgSemAlt', 'img sem alt'), ('imgQuebrada', 'img quebrada'), ('secaoEstreita', 'seção não full-bleed'),
                     ('toque', 'alvo de toque < 44px'), ('console', 'erro de console'), ('falhas', 'requisição falhou'),
                     ('invisiveis', 'conteúdo invisível')):
        if r[k]:
            p.append(f'{label}: {r[k]}')
    if mode in ('padrao', 'escuro', 'arquivo') and not r['motion']:
        p.append('motion não iniciou')
    if mode == 'reduzido' and (not r['motion'] or r['motion']['modo'] != 'reduced'):
        p.append(f"modo reduzido não aplicado: {r['motion']}")
    return p


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, 'screenshots', 'auditoria-final')
    os.makedirs(out, exist_ok=True)
    httpd = ThreadingHTTPServer(('127.0.0.1', PORT), Silent)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    report, total, falhou = {}, 0, 0
    with sync_playwright() as pw:
        for engine in ('chromium', 'webkit'):
            browser = getattr(pw, engine).launch()
            modes = ['padrao', 'reduzido', 'escuro', 'sem-js'] + (['arquivo'] if engine == 'chromium' else [])
            for mode in modes:
                for w, h in RES:
                    key = f'{engine}/{mode}/{w}x{h}'
                    try:
                        r = run_combo(browser, engine, mode, w, h, os.path.join(out, 'telas'))
                        p = problemas(r, mode)
                    except Exception as e:  # registra e segue
                        r, p = {'erro': str(e)[:300]}, [f'falha na execução: {str(e)[:200]}']
                    report[key] = {'resultado': r, 'problemas': p}
                    total += 1
                    if p:
                        falhou += 1
                        print(f'FAIL {key}: ' + ' | '.join(p))
                print(f'{engine}/{mode}: concluído')
            browser.close()
    httpd.shutdown()
    json.dump(report, open(os.path.join(out, 'relatorio.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'\nRESUMO: {total - falhou}/{total} combinações sem problema ({falhou} com problema)')


if __name__ == '__main__':
    main()
