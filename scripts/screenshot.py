import sys
import os
import time
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler
from playwright.sync_api import sync_playwright

PORT = 8765
HOST = '127.0.0.1'

class SilentHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='site', **kwargs)
    def log_message(self, format, *args):
        pass  # silenciar logs

def run_server(httpd):
    httpd.serve_forever()

def capture(section_id=None, prev_section_id=None):
    os.makedirs('screenshots', exist_ok=True)
    httpd = HTTPServer((HOST, PORT), SilentHandler)
    server_thread = threading.Thread(target=run_server, args=(httpd,), daemon=True)
    server_thread.start()

    url = f'http://{HOST}:{PORT}/index.html'

    viewports = {
        '1440': {'width': 1440, 'height': 900},
        '390': {'width': 390, 'height': 844},
    }

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        
        for vp_name, vp_size in viewports.items():
            page = browser.new_page(viewport=vp_size)
            page.goto(url, wait_until='networkidle')
            time.sleep(0.5)

            # 1. Página Inteira
            full_path = f'screenshots/full_{vp_name}.png'
            page.screenshot(path=full_path, full_page=True)
            print(f'Full page captured: {full_path}')

            # 2. Seção Isolada (se especificada)
            if section_id:
                elem = page.locator(f'#{section_id}')
                if elem.count() > 0:
                    sec_path = f'screenshots/{section_id}_{vp_name}.png'
                    elem.screenshot(path=sec_path)
                    print(f'Section captured: {sec_path}')
                else:
                    print(f'Warning: section #{section_id} not found')

            # 3. Costura / Transição com a anterior (se houver)
            if section_id and prev_section_id:
                prev_elem = page.locator(f'#{prev_section_id}')
                curr_elem = page.locator(f'#{section_id}')
                if prev_elem.count() > 0 and curr_elem.count() > 0:
                    prev_box = prev_elem.bounding_box()
                    curr_box = curr_elem.bounding_box()
                    if prev_box and curr_box:
                        # Região de transição: últimos 250px da anterior e primeiros 250px da atual
                        top = max(0, curr_box['y'] - 220)
                        bottom = curr_box['y'] + 220
                        height = bottom - top
                        seam_path = f'screenshots/{section_id}_seam_{vp_name}.png'
                        page.screenshot(
                            path=seam_path,
                            clip={'x': 0, 'y': top, 'width': vp_size['width'], 'height': height}
                        )
                        print(f'Seam captured: {seam_path}')

            page.close()

        browser.close()
    httpd.shutdown()

if __name__ == '__main__':
    sec = sys.argv[1] if len(sys.argv) > 1 else None
    prev_sec = sys.argv[2] if len(sys.argv) > 2 else None
    capture(sec, prev_sec)
