from http.server import SimpleHTTPRequestHandler, HTTPServer
import logging

logging.basicConfig(level=logging.INFO)
class MyHandler(SimpleHTTPRequestHandler)
    def do_GET(self):
        logging.info(f"Recieved Get Request")

        if self.path == '/':
            self.path = '../index.html'
        elif self.path == '/about':
            self.path = '../about.html'
        elif self.path == '../tech-tutorials':
            self.path = '../tech-tutorials.html'
        elif self.path == '/login-register':
            self.path == '../login-register.html'
        elif self.path == '/safety':
            self.path = '../safety.html'
        else:
            self.path = '../404.html'
        return super().do_GET()
    
    def do_POST(self):
    content_length = int(self.headers['Content-Length'])
    post_data = self.rfile.read(content_length).decode('utf-8')
    logging.info(f"Received POST data: {post_data}")
    self.send_response(200)
    self.end_headers()
    self.wfile.write(b"Form submitted successfully!")

    if __name__ == "__main__":
    server_address = ('', 8000)  # Localhost, port 8000
    httpd = HTTPServer(server_address, MyHandler)
    logging.info("Server running on http://localhost:8000")
    httpd.serve_forever()