import http.server

class CORSServer(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

http.server.test(CORSServer, http.server.HTTPServer, port=4000)
