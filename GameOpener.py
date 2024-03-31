import http.server
import socketserver
import webbrowser
import os
import sys


Port = 8000

if len(sys.argv) < 2:
    print("Usage: python GameOpener.py <path>")
    sys.exit(1)


game_dir = sys.argv[1]

os.chdir(game_dir)
handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", Port), handler) as httpd:
    print("serving at port", Port)
    httpd.serve_forever()