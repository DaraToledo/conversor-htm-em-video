#!/usr/bin/env python3
"""
Servidor local para o conversor HTML → Vídeo
Execute este arquivo e abra: http://localhost:8080
"""
import http.server
import socketserver
import webbrowser
import os
import sys
from pathlib import Path

PORT = 8080
DIRECTORY = Path(__file__).parent

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIRECTORY), **kwargs)
    
    def end_headers(self):
        # Permite que iframes acessem recursos locais
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()
    
    def log_message(self, format, *args):
        print(f"  [{self.address_string()}] {format % args}")

url = f"http://localhost:{PORT}/html-to-video.html"

print("=" * 55)
print("   🎬  Conversor HTML → Vídeo — Servidor Local")
print("=" * 55)
print(f"\n  ✅  Servidor iniciado em: {url}")
print(f"  📁  Pasta servida: {DIRECTORY}")
print(f"\n  Abrindo o navegador automaticamente...")
print(f"\n  Para parar: pressione CTRL+C")
print("-" * 55)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    webbrowser.open(url)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n  Servidor encerrado. Até mais!")
        sys.exit(0)
