import os
import subprocess
import threading
import time
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8789
HOST = '127.0.0.1'

class SilentHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='site', **kwargs)
    def log_message(self, format, *args):
        pass

def run():
    httpd = HTTPServer((HOST, PORT), SilentHandler)
    server_thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    server_thread.start()
    time.sleep(1)

    url = f'http://{HOST}:{PORT}/index.html'
    out_file = 'lighthouse_mobile.json'

    # Run lighthouse via npx
    cmd = [
        'npx.cmd',
        'lighthouse',
        url,
        '--form-factor=mobile',
        '--throttling.rttMs=150',
        '--throttling.throughputKbps=1638.4',
        '--output=json',
        f'--output-path={out_file}',
        '--chrome-flags=--headless --no-sandbox',
        '--only-categories=performance,accessibility,best-practices,seo',
        '--quiet'
    ]

    print('Running Lighthouse mobile audit...')
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        print('STDOUT:', proc.stdout[:500])
        print('STDERR:', proc.stderr[:500])
        print('Return code:', proc.returncode)
    except Exception as e:
        print('Exception running lighthouse:', e)

    httpd.shutdown()

if __name__ == '__main__':
    run()
