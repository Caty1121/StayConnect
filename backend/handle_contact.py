from http.server import SimpleHTTPRequestHandler, HTTPServer
import urllib.parse
import sqlite3
import logging

logging.basicConfig(level=logging.INFO)

class ContactHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/submit_contact':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            parsed = urllib.parse.parse_qs(post_data)

            first_name = parsed.get('fName', [''])[0]
            last_name = parsed.get('lName', [''])[0]
            phone = parsed.get('phone1', [''])[0]
            email = parsed.get('email', [''])[0]
            message = parsed.get('details', [''])[0]
            confirmed = 1 if parsed.get('confirm', ['0'])[0] == '1' else 0

            conn = sqlite3.connect('stayconnect.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO contact_messages (first_name, last_name, phone, email, message, confirmed)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (first_name, last_name, phone, email, message.strip(), confirmed))
            conn.commit()
            conn.close()

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Thanks for contacting us!")
        elif self.path == '/register_user':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            parsed = urllib.parse.parse_qs(post_data)

            first_name = parsed.get('first_name', [''])[0]
            last_name = parsed.get('last_name', [''])[0]
            email = parsed.get('email', [''])[0]
            password = parsed.get('password', [''])[0]

            conn = sqlite3.connect('stayconnect.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO users (first_name, last_name, email, password)
                VALUES (?, ?, ?, ?)
            ''', (first_name, last_name, email, password))
            conn.commit()
            conn.close()

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Registration successful!")


        else:
            self.send_error(404, "Not Found")

if __name__ == "__main__":
    server_address = ('', 8001)
    httpd = HTTPServer(server_address, ContactHandler)
    logging.info("Server running on http://localhost:8001")
    httpd.serve_forever()
