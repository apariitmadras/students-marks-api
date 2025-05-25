import json
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

with open("data/marks.json", "r") as f:
    marks_data = json.load(f)

marks_dict = {entry["name"]: entry["marks"] for entry in marks_data}

class handler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers()

    def do_GET(self):
        self._set_headers()

        query = parse_qs(urlparse(self.path).query)
        names = query.get("name", [])
        result = [marks_dict.get(name, None) for name in names]

        self.wfile.write(json.dumps({"marks": result}).encode())
