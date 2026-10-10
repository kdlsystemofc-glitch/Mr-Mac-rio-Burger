import os
import sys
import time
import threading
# ThreadingHTTPServer: o HTTPServer de thread única recusava conexões (fila de 5) quando o Chrome abria 6 em paralelo
from http.server import ThreadingHTTPServer as HTTPServer, SimpleHTTPRequestHandler
from playwright.sync_api import sync_playwright

PORT = 8788
HOST = '127.0.0.1'

class SilentHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='site', **kwargs)
    def log_message(self, format, *args):
        pass

def run():
    os.makedirs('screenshots/responsive', exist_ok=True)
    httpd = HTTPServer((HOST, PORT), SilentHandler)
    server_thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    server_thread.start()

    url = f'http://{HOST}:{PORT}/index.html'

    resolutions = [
        ('2560x1440', 2560, 1440),
        ('1920x1080', 1920, 1080),
        ('1440x900',  1440, 900),
        ('1366x768',  1366, 768),
        ('1280x720',  1280, 720),
        ('1024x768',  1024, 768),
        ('768x1024',  768,  1024),
        ('430x932',   430,  932),
        ('390x844',   390,  844),
        ('360x740',   360,  740),
        ('320x568',   320,  568),
        ('844x390',   844,  390), # landscape
    ]

    all_passed = True

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        for label, w, h in resolutions:
            console_errors = []
            page = browser.new_page(viewport={'width': w, 'height': h})

            page.on('console', lambda msg: console_errors.append(f'[{msg.type}] {msg.text}') if msg.type == 'error' else None)
            page.on('pageerror', lambda err: console_errors.append(f'[EXCEPTION] {str(err)}'))

            page.goto(url, wait_until='networkidle')
            time.sleep(0.4)

            # 1. Checar Rolagem Horizontal
            scroll_data = page.evaluate("""() => {
                const doc = document.documentElement;
                const body = document.body;
                const docScrollW = doc.scrollWidth;
                const docClientW = doc.clientWidth;
                const bodyScrollW = body.scrollWidth;
                const bodyClientW = body.clientWidth;
                return {
                    docOverflow: docScrollW - docClientW,
                    bodyOverflow: bodyScrollW - bodyClientW,
                    docScrollW, docClientW
                };
            }""")

            has_hscroll = scroll_data['docOverflow'] > 1 or scroll_data['bodyOverflow'] > 1

            # 2. Checar Alvos de Toque (min 44x44px nos elementos visíveis)
            touch_targets = page.evaluate("""() => {
                const interactives = Array.from(document.querySelectorAll('a, button'));
                const results = [];
                for (const el of interactives) {
                    const rect = el.getBoundingClientRect();
                    const style = window.getComputedStyle(el);
                    if (style.display !== 'none' && style.visibility !== 'hidden' && rect.width > 0 && rect.height > 0) {
                        const meetsReq = rect.width >= 43.5 && rect.height >= 43.5;
                        if (!meetsReq) {
                            results.push({
                                tag: el.tagName,
                                text: el.innerText.trim().substring(0, 30),
                                class: el.className,
                                w: Math.round(rect.width),
                                h: Math.round(rect.height)
                            });
                        }
                    }
                }
                return results;
            }""")

            # 3. Screenshot
            out_file = f'screenshots/responsive/{label}.png'
            page.screenshot(path=out_file, full_page=True)

            status_scroll = "PASS" if not has_hscroll else f"FAIL (+{scroll_data['docOverflow']}px)"
            status_console = "PASS" if len(console_errors) == 0 else f"FAIL ({len(console_errors)} errors)"
            status_touch = "PASS" if len(touch_targets) == 0 else f"WARN ({len(touch_targets)} small targets: {touch_targets})"

            print(f"[{label}] Scroll: {status_scroll} | Console: {status_console} | Touch: {status_touch} -> {out_file}")

            if has_hscroll or len(console_errors) > 0:
                all_passed = False

            page.close()

        # Teste de Zoom de Texto a 200%
        print("\n--- Testando Zoom de Texto a 200% ---")
        zoom_page = browser.new_page(viewport={'width': 1280, 'height': 720})
        zoom_page.goto(url, wait_until='networkidle')
        zoom_page.evaluate("document.documentElement.style.fontSize = '32px';") # 200% text zoom
        time.sleep(0.5)
        zoom_scroll = zoom_page.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
        zoom_page.screenshot(path='screenshots/responsive/zoom_200.png', full_page=True)
        print(f"Zoom 200%: Overflow={zoom_scroll}px (PASS if <= 1px)")
        zoom_page.close()

        # Teste de Prefers-Reduced-Motion
        print("\n--- Testando Prefers-Reduced-Motion ---")
        prm_page = browser.new_page(viewport={'width': 1440, 'height': 900}, reduced_motion='reduce')
        prm_page.goto(url, wait_until='networkidle')
        prm_page.screenshot(path='screenshots/responsive/reduced_motion.png', full_page=True)
        print("Reduced motion: Teste renderizado com sucesso")
        prm_page.close()

        # Teste de Prefers-Color-Scheme Dark
        print("\n--- Testando Prefers-Color-Scheme Dark ---")
        dark_page = browser.new_page(viewport={'width': 1440, 'height': 900}, color_scheme='dark')
        dark_page.goto(url, wait_until='networkidle')
        dark_page.screenshot(path='screenshots/responsive/dark_scheme.png', full_page=True)
        print("Color scheme dark: Teste renderizado com sucesso")
        dark_page.close()

        browser.close()

    httpd.shutdown()
    print("\nAuditoria Responsiva Concluída!")

if __name__ == '__main__':
    run()
