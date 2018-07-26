from http.server import HTTPServer, BaseHTTPRequestHandler


class Server(BaseHTTPRequestHandler):

    def do_GET(self): #Overriding BaseHTTPRequestHandler
        if self.path == '/':
            self.path = '/index.html'
        try:
            file = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file, 'utf-8'))


httpd = HTTPServer(('10.0.1.46', 8080), Server)
httpd.serve_forever()
