import os
import time
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler
from playwright.sync_api import sync_playwright

PORT = 8769
HOST = '127.0.0.1'

class SilentHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='site', **kwargs)
    def log_message(self, format, *args):
        pass

def run():
    os.makedirs('screenshots', exist_ok=True)
    httpd = HTTPServer((HOST, PORT), SilentHandler)
    server_thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    server_thread.start()

    url = f'http://{HOST}:{PORT}/index.html'
    viewports = {
        '1440': {'width': 1440, 'height': 900},
        '768': {'width': 768, 'height': 1024},
        '390': {'width': 390, 'height': 844},
    }

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        for name, size in viewports.items():
            page = browser.new_page(viewport=size)
            page.goto(url, wait_until='networkidle')
            time.sleep(1.0)
            out_file = f'screenshots/final_full_{name}.png'
            page.screenshot(path=out_file, full_page=True)
            print(f'Captured: {out_file}')
            page.close()
        browser.close()

    httpd.shutdown()

if __name__ == '__main__':
    run()
