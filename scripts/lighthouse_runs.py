"""Roda o Lighthouse mobile N vezes contra site/ servido por HTTP e imprime a mediana.

Uso: python scripts/lighthouse_runs.py <saida_prefixo> [n_execucoes] [--prod]
  --prod: simula o servidor de produção recomendado em DEPLOY.md (gzip em texto + Cache-Control).
          Sem a flag: http.server puro, igual à medição da baseline.
Gera <saida_prefixo>-N.json e imprime scores/métricas de cada execução + mediana.
Mesmos parâmetros do run_lighthouse.py original (mobile, RTT 150ms, 1.6 Mbps, CPU 4x simulado).
"""
import gzip
import json
import os
import statistics
import subprocess
import sys
import threading
from http.server import ThreadingHTTPServer as HTTPServer, SimpleHTTPRequestHandler

PORT = 8789
HOST = '127.0.0.1'
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'


class SilentHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='site', **kwargs)

    def log_message(self, format, *args):
        pass


TEXT_TYPES = ('.html', '.css', '.js', '.svg')


class ProdHandler(SilentHandler):
    """gzip em texto + Cache-Control conforme DEPLOY.md."""

    def do_GET(self):
        path = self.translate_path(self.path.split('?')[0])
        if os.path.isdir(path):
            path = os.path.join(path, 'index.html')
        if not os.path.isfile(path):
            return super().do_GET()
        data = open(path, 'rb').read()
        ctype = self.guess_type(path)
        self.send_response(200)
        self.send_header('Content-Type', ctype)
        rel = path.replace(os.sep, '/')
        if rel.endswith('.html'):
            cc = 'no-cache'
        elif '/fonts/' in rel:
            cc = 'public, max-age=31536000, immutable'
        elif '/js/vendor/' in rel:
            cc = 'public, max-age=2592000'
        elif rel.endswith(('.css', '.js')):
            cc = 'public, max-age=86400, stale-while-revalidate=604800'
        else:
            cc = 'public, max-age=2592000, stale-while-revalidate=86400'
        self.send_header('Cache-Control', cc)
        if path.endswith(TEXT_TYPES) and 'gzip' in self.headers.get('Accept-Encoding', ''):
            data = gzip.compress(data, 9)
            self.send_header('Content-Encoding', 'gzip')
            self.send_header('Vary', 'Accept-Encoding')
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)


METRICS = ['first-contentful-paint', 'largest-contentful-paint', 'total-blocking-time',
           'cumulative-layout-shift', 'speed-index']


def main():
    prefix = sys.argv[1]
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    handler = ProdHandler if '--prod' in sys.argv else SilentHandler
    httpd = HTTPServer((HOST, PORT), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    env = dict(os.environ, CHROME_PATH=CHROME)
    results = []
    for i in range(1, n + 1):
        out = f'{prefix}-{i}.json'
        cmd = [os.path.join('node_modules', '.bin', 'lighthouse.cmd'), f'http://{HOST}:{PORT}/' + os.environ.get('LH_PAGE', 'index.html'),
               '--form-factor=mobile', '--throttling.rttMs=150', '--throttling.throughputKbps=1638.4',
               '--output=json', f'--output-path={out}',
               '--chrome-flags=--headless=new --no-sandbox --disable-gpu',
               '--only-categories=performance,accessibility,best-practices,seo', '--quiet']
        subprocess.run(cmd, env=env, timeout=240)
        with open(out, encoding='utf-8') as f:
            d = json.load(f)
        r = {k: round(v['score'] * 100) for k, v in d['categories'].items()}
        for m in METRICS:
            r[m] = d['audits'][m]['numericValue']
        results.append(r)
        print(f'run {i}:', r)
    httpd.shutdown()
    med = {k: statistics.median(r[k] for r in results) for k in results[0]}
    print('MEDIAN:', json.dumps(med))


if __name__ == '__main__':
    main()
