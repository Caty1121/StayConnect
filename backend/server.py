from http.server import SimpleHTTPRequestHandler, HTTPServer
import logging
import os

logging.basicConfig(level=logging.INFO)

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        logging.info(f"Received GET request for {self.path}")

        if self.path == '/':
            self.path = 'index.html'
        elif self.path == '/about':
            self.path = 'about.html'
        elif self.path == '/tech-tutorials':
            self.path = 'tech-tutorials.html'
        elif self.path == '/login-register':
            self.path = 'login-register.html'
        elif self.path == '/safety':
            self.path = 'safety.html'
        else:
            pass

        return super().do_GET()

    def translate_path(self, path):
        root = os.path.abspath(os.path.dirname(__file__))
        root = os.path.join(root, '..')
        return os.path.join(root, path.lstrip('/'))

if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    logging.info("Server running on http://localhost:8000")
    httpd.serve_forever()
