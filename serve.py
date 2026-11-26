#!/usr/bin/env python3
"""Lokalni server za EW Skener.

Treba ti samo ako browser blokira direktne pozive ka api.bybit.com (CORS).
Pokretanje:  python3 serve.py   (ili dupli klik na Windowsu)
Zatim otvori http://127.0.0.1:8765/ew-skener.html

Server prosleđuje samo javne GET zahteve /bybit/v5/market/* ka api.bybit.com.
Nema ključeva, nema naloga, ništa se ne šalje osim zahteva za tržišne podatke.
"""
import http.server
import os
import urllib.error
import urllib.request
import webbrowser

PORT = 8765
UPSTREAM = "https://api.bybit.com"
PREFIX = "/bybit/v5/market/"


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith(PREFIX):
            return self.proxy()
        return super().do_GET()

    def proxy(self):
        url = UPSTREAM + self.path[len("/bybit"):]
        req = urllib.request.Request(url, headers={"User-Agent": "ew-skener/1.0"})
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                body, status = r.read(), r.status
        except urllib.error.HTTPError as e:
            body, status = e.read(), e.code
        except Exception as e:  # mreža nedostupna
            body, status = ('{"retCode":-1,"retMsg":"%s"}' % type(e).__name__).encode(), 502
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    link = f"http://127.0.0.1:{PORT}/ew-skener.html"
    print(f"EW Skener radi na {link}  (Ctrl+C za kraj)")
    try:
        webbrowser.open(link)
    except Exception:
        pass
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass
