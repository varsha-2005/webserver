from http.server import HTTPServer,BaseHTTPRequestHandler

content ="""
<DOCTYPE HTML>
<html>
<head>
<title>My webserver</title>
</head>
<body>
<h1>Welcome to the webserver </h1>
</body>
</html>
"""

class WebHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type','text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
    
server_address=('',8080)
httpd = HTTPServer(server_address,WebHandler)
print("my webserver is running...")
httpd.serve_forever()