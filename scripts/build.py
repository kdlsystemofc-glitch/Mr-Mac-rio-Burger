"""build.py — gera o site publicável em site/ a partir de src/.

Uso: python scripts/build.py      (ou: npm run build)

Entradas (editar aqui):  src/index.html, src/css/*.css, src/js/*.js
Saídas (não editar):     site/index.html, site/styles.min.css, site/js/motion-*.min.js
Estáticos (ficam em site/): assets/, fonts/, js/vendor/

Passos:
1. Junta fonts + tokens + reset + style em um CSS só e minifica (clean-css nível 1, preserva fallbacks).
2. CSS crítico por medição: abre a página com o CSS completo nas 12 resoluções da regressão + a do
   Lighthouse e guarda toda regra cujo seletor casa com algum elemento visível na primeira tela
   (sem rolar, sem JS). @media/@supports são filtrados por dentro; @keyframes entram se citados.
   O CSS completo carrega depois, sem bloquear, e repete essas regras na ordem original — então o
   resultado final da cascata é idêntico ao de antes (crítico só antecipa).
3. Verifica: estilos computados de todos os elementos da primeira tela com só o crítico == com o
   completo, em todas as resoluções. Diferença = build falha.
4. Minifica JS próprio (terser) e o carregador inline; relata pesos (bruto e gzip).
"""
import gzip
import json
import os
import re
import subprocess
import sys
import tempfile
import threading
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

import tinycss2
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'src')
SITE = os.path.join(ROOT, 'site')
CSS_ORDER = ['fonts.css', 'tokens.css', 'reset.css', 'style.css']
JS_FILES = ['motion-core.js', 'motion-sections.js']
VIEWPORTS = [(2560, 1440), (1920, 1080), (1440, 900), (1366, 768), (1280, 720), (1024, 768),
             (768, 1024), (430, 932), (390, 844), (360, 740), (320, 568), (844, 390), (412, 823)]
PORT = 8791
# 15% além da dobra: folga para métricas de fonte/barras de navegador de outros aparelhos
FOLD_MARGIN = 1.15
CRIT_MARK = '<!-- @build:critical-css (gerado por scripts/build.py a partir de src/css/) -->'
STYLES_MARK = '<!-- @build:styles -->'
# Pseudo-classes/elementos que dependem de estado ou não existem no DOM: removidos só para testar casamento
PSEUDO_RE = re.compile(r'::?(?:hover|focus-visible|focus-within|focus|active|visited|link|before|after|'
                       r'placeholder|selection|marker|first-letter|first-line|-webkit-[a-z-]+|-moz-[a-z-]+)'
                       r'(?![\w-])')


def node(*args):
    subprocess.run(['node', os.path.join(ROOT, 'scripts', 'minify.cjs'), *args], check=True)


def minify_css_text(text):
    with tempfile.TemporaryDirectory() as d:
        i, o = os.path.join(d, 'in.css'), os.path.join(d, 'out.css')
        open(i, 'w', encoding='utf-8').write(text)
        node('css', i, o)
        return open(o, encoding='utf-8').read()


def minify_js_text(text):
    with tempfile.TemporaryDirectory() as d:
        i, o = os.path.join(d, 'in.js'), os.path.join(d, 'out.js')
        open(i, 'w', encoding='utf-8').write(text)
        node('js', i, o)
        return open(o, encoding='utf-8').read()


def split_selectors(prelude):
    """Divide 'a, b:not(.x, .y)' só nas vírgulas de nível 0."""
    out, depth, cur = [], 0, ''
    for ch in prelude:
        if ch in '([':
            depth += 1
        elif ch in ')]':
            depth -= 1
        if ch == ',' and depth == 0:
            out.append(cur.strip())
            cur = ''
        else:
            cur += ch
    if cur.strip():
        out.append(cur.strip())
    return out


def collect_rules(nodes, path, rules):
    """Indexa toda qualified rule (inclusive dentro de @media/@supports) -> lista de seletores."""
    for idx, n in enumerate(nodes):
        if n.type == 'qualified-rule':
            sels = [PSEUDO_RE.sub('', s).strip() or '*' for s in split_selectors(tinycss2.serialize(n.prelude))]
            rules[path + (idx,)] = sels
        elif n.type == 'at-rule' and n.lower_at_keyword in ('media', 'supports') and n.content is not None:
            collect_rules(tinycss2.parse_rule_list(n.content), path + (idx,), rules)


class SourceText:
    """Recorta o texto ORIGINAL de cada regra (tinycss2.serialize normaliza aspas e espaços)."""

    def __init__(self, text):
        self.text = text
        self.line_starts = [0] + [m.end() for m in re.finditer('\n', text)]

    def offset(self, node):
        return self.line_starts[node.source_line - 1] + node.source_column - 1

    def block_bounds(self, node):
        """(início, posição do '{', posição do '}' correspondente), pulando strings e comentários."""
        t, i = self.text, self.offset(node)
        start, depth, open_pos, quote = i, 0, None, None
        while i < len(t):
            c = t[i]
            if quote:
                if c == '\\':
                    i += 1
                elif c == quote:
                    quote = None
            elif t.startswith('/*', i):
                i = t.index('*/', i + 2) + 1
            elif c in '"\'':
                quote = c
            elif c == '{':
                if depth == 0:
                    open_pos = i
                depth += 1
            elif c == '}':
                depth -= 1
                if depth == 0:
                    return start, open_pos, i
            i += 1
        raise ValueError('bloco CSS sem fechamento')

    def rule(self, node):
        s, _, e = self.block_bounds(node)
        return self.text[s:e + 1]

    def head(self, node):
        s, o, _ = self.block_bounds(node)
        return self.text[s:o]


def emit(src, nodes, path, keep, keyframe_names, font_families):
    """Monta o CSS crítico com o texto original de cada regra, na ordem original."""
    parts = []
    for idx, n in enumerate(nodes):
        p = path + (idx,)
        if n.type == 'qualified-rule' and p in keep:
            parts.append(src.rule(n))
        elif n.type == 'at-rule':
            kw = n.lower_at_keyword
            if kw == 'font-face':
                # só famílias usadas por texto visível na primeira tela (as demais vêm no CSS completo)
                fam = re.search(r'font-family\s*:\s*[\'"]?([^;\'"]+)', src.rule(n)).group(1).strip()
                if fam in font_families:
                    parts.append(src.rule(n))
            elif kw in ('media', 'supports') and n.content is not None:
                inner = emit(src, tinycss2.parse_rule_list(n.content), p, keep, keyframe_names, font_families)
                if inner.strip():
                    parts.append(src.head(n) + '{\n' + inner + '\n}')
            elif kw in ('keyframes', '-webkit-keyframes'):
                name = tinycss2.serialize(n.prelude).strip()
                if name in keyframe_names:
                    parts.append(src.rule(n))
    return '\n'.join(parts)


class Silent(SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=SITE, **k)

    def log_message(self, *a):
        pass


FAMILIES_JS = """() => {
  const out = new Set();
  const tw = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  let n;
  while ((n = tw.nextNode())) {
    const el = n.parentElement;
    if (!n.nodeValue.trim() || el.closest('script, noscript, style')) continue;
    const r = el.getBoundingClientRect();
    if (r.top < innerHeight && r.bottom > 0 && r.width > 0)
      out.add(getComputedStyle(el).fontFamily.split(',')[0].replace(/["']/g, '').trim());
  }
  return [...out];
}"""


STYLE_SNAPSHOT_JS = """() => {
  const LAYOUT_DERIVED = ['height', 'block-size', 'perspective-origin', 'transform-origin'];
  const out = {};
  const els = [document.documentElement, document.body, ...document.body.querySelectorAll('*')];
  els.forEach((el, i) => {
    if (el.closest('script, noscript, style')) return;
    const r = el.getBoundingClientRect();
    const container = el === document.documentElement || el === document.body || el.tagName === 'MAIN';
    if (!container && !(r.top < innerHeight && r.bottom > 0)) return;
    for (const pseudo of [null, '::before', '::after']) {
      const cs = getComputedStyle(el, pseudo);
      const o = {};
      for (let k = 0; k < cs.length; k++) {
        const p = cs[k];
        // altura de html/body/main depende do conteúdo abaixo da dobra (esperado enquanto o CSS completo não chega)
        if (container && LAYOUT_DERIVED.includes(p)) continue;
        // margem 'auto' resolvida é instável no getComputedStyle do Chrome (0px ou o valor usado, ao acaso);
        // margens são conferidas pela geometria real (__rect) logo abaixo
        if (p.startsWith('margin')) continue;
        o[p] = cs.getPropertyValue(p);
      }
      if (!pseudo && !container) o.__rect = [r.x, r.y, r.width, r.height].map((v) => v.toFixed(2)).join(',');
      out[i + (pseudo || '')] = o;
    }
  });
  return out;
}"""


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    template = open(os.path.join(SRC, 'index.html'), encoding='utf-8').read()
    assert CRIT_MARK in template and STYLES_MARK in template, 'marcadores de build ausentes em src/index.html'

    # 1. CSS completo
    full_src = '\n'.join(open(os.path.join(SRC, 'css', f), encoding='utf-8').read() for f in CSS_ORDER)
    full_min = minify_css_text(full_src)
    open(os.path.join(SITE, 'styles.min.css'), 'w', encoding='utf-8').write(full_min)

    sheet = tinycss2.parse_stylesheet(full_src, skip_comments=True, skip_whitespace=True)
    src_text = SourceText(full_src)
    rules = {}
    collect_rules(sheet, (), rules)
    rule_list = [[list(k), v] for k, v in rules.items()]

    # Página de sondagem: CSS completo, sem o carregador de motion (estado estático, sem JS)
    body_html = re.sub(r'<script>.*?</script>', '', template, flags=re.S)
    probe_full = body_html.replace(CRIT_MARK, '').replace(STYLES_MARK, '<link rel="stylesheet" href="./styles.min.css">')
    httpd = ThreadingHTTPServer(('127.0.0.1', PORT), Silent)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    probe_path = os.path.join(SITE, '__build_probe.html')
    keep = set()
    families = set()
    try:
        with sync_playwright() as pw:
            browser = pw.chromium.launch()
            open(probe_path, 'w', encoding='utf-8').write(probe_full)
            for w, h in VIEWPORTS:
                pg = browser.new_page(viewport={'width': w, 'height': h})
                pg.goto(f'http://127.0.0.1:{PORT}/__build_probe.html', wait_until='networkidle')
                pg.evaluate('document.fonts.ready')
                hits = pg.evaluate("""([rules, FOLD_MARGIN]) => {
                  const vis = (el) => {
                    if (el === document.documentElement || el === document.body) return true;
                    // sem caixa (display:none) conta se o pai está na primeira tela: a regra que o esconde é crítica
                    if (el.getClientRects().length === 0) return !!el.parentElement && vis(el.parentElement);
                    const r = el.getBoundingClientRect();
                    return r.top < innerHeight * FOLD_MARGIN && r.bottom > 0;
                  };
                  const hit = [];
                  for (const [key, sels] of rules) {
                    let ok = false;
                    for (const s of sels) {
                      let els;
                      try { els = document.querySelectorAll(s); } catch (e) { continue; }
                      for (const el of els) { if (vis(el)) { ok = true; break; } }
                      if (ok) break;
                    }
                    if (ok) hit.push(key);
                  }
                  return hit;
                }""", [rule_list, FOLD_MARGIN])
                keep.update(tuple(k) for k in hits)
                families.update(pg.evaluate(FAMILIES_JS))
                pg.close()

            # 2. Monta o crítico
            keyframe_names = {tinycss2.serialize(n.prelude).strip() for n in sheet
                              if n.type == 'at-rule' and n.lower_at_keyword in ('keyframes', '-webkit-keyframes')}
            # crítico provisório só para descobrir quais @keyframes ele cita
            draft = emit(src_text, sheet, (), keep, set(), families)
            used_kf = {k for k in keyframe_names if re.search(r'(?<![\w-])' + re.escape(k) + r'(?![\w-])', draft)}
            critical = minify_css_text(emit(src_text, sheet, (), keep, used_kf, families))
            print('Fontes com @font-face no crítico:', sorted(families))

            # 3. Verificação: só-crítico == completo, nos elementos da primeira tela
            probe_crit = body_html.replace(CRIT_MARK, '<style>' + critical + '</style>').replace(STYLES_MARK, '')
            crit_html = probe_crit
            mismatches = []
            for w, h in VIEWPORTS:
                snaps = []
                for html in (probe_full, crit_html):
                    open(probe_path, 'w', encoding='utf-8').write(html)
                    pg = browser.new_page(viewport={'width': w, 'height': h})
                    pg.goto(f'http://127.0.0.1:{PORT}/__build_probe.html', wait_until='networkidle')
                    pg.evaluate('document.fonts.ready')
                    snaps.append(pg.evaluate(STYLE_SNAPSHOT_JS))
                    pg.close()
                full_s, crit_s = snaps
                for el, props in full_s.items():
                    other = crit_s.get(el)
                    if other is None:
                        mismatches.append(f'{w}x{h} {el}: ausente só com crítico')
                        continue
                    for p, v in props.items():
                        if other.get(p) != v:
                            mismatches.append(f'{w}x{h} el#{el} {p}: completo={v!r} critico={other.get(p)!r}')
            browser.close()
    finally:
        httpd.shutdown()
        if os.path.exists(probe_path):
            os.remove(probe_path)
    if mismatches:
        print('\n'.join(mismatches[:40]))
        sys.exit(f'FALHA: {len(mismatches)} diferenças entre CSS crítico e completo')
    print(f'CSS crítico verificado em {len(VIEWPORTS)} resoluções: estilos computados idênticos '
          f'({len(keep)}/{len(rules)} regras).')

    # 4. JS próprio
    os.makedirs(os.path.join(SITE, 'js'), exist_ok=True)
    for f in JS_FILES:
        node('js', os.path.join(SRC, 'js', f), os.path.join(SITE, 'js', f.replace('.js', '.min.js')))

    def min_inline_script(m):
        return '<script>' + minify_js_text(m.group(1)) + '</script>'

    html = re.sub(r'<script>(.*?)</script>', min_inline_script, template, flags=re.S)
    # media=print: baixa sem bloquear. No onload, aplica só depois do próximo quadro pintado (duplo rAF):
    # o recálculo de estilo/layout da página inteira não atrasa a primeira pintura do hero.
    # Sem JS: o <noscript> carrega o mesmo arquivo de forma bloqueante (comportamento clássico).
    styles_tag = ('<link rel="stylesheet" href="./styles.min.css" media="print" onload="var l=this;l.onload=null;'
                  'requestAnimationFrame(function(){requestAnimationFrame(function(){l.media=\'all\'})})">\n'
                  '  <noscript><link rel="stylesheet" href="./styles.min.css"></noscript>')
    html = html.replace(CRIT_MARK, '<style>' + critical + '</style>').replace(STYLES_MARK, styles_tag)
    html = ('<!-- GERADO por scripts/build.py — não editar. Fonte: src/index.html -->\n' + html)
    open(os.path.join(SITE, 'index.html'), 'w', encoding='utf-8').write(html)

    # Relatório de pesos
    def report(label, data):
        b = data if isinstance(data, bytes) else data.encode('utf-8')
        print(f'  {label:<34} {len(b) / 1024:7.1f} KB   gzip {len(gzip.compress(b, 9)) / 1024:6.1f} KB')

    print('Pesos:')
    report('index.html (com crítico inline)', html)
    report('  └ CSS crítico inline', critical)
    report('styles.min.css', full_min)
    for f in JS_FILES:
        src_b = open(os.path.join(SRC, 'js', f), 'rb').read()
        out_b = open(os.path.join(SITE, 'js', f.replace('.js', '.min.js')), 'rb').read()
        report(f'src/js/{f} (fonte)', src_b)
        report(f'js/{f.replace(".js", ".min.js")}', out_b)
    for f in sorted(os.listdir(os.path.join(SITE, 'js', 'vendor'))):
        report(f'js/vendor/{f}', open(os.path.join(SITE, 'js', 'vendor', f), 'rb').read())


if __name__ == '__main__':
    main()
