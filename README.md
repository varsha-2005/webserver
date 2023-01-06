# Developing a Simple Webserver

# AIM:

To develop a simple webserver to display about top five programming
languages.

## DESIGN STEPS:

### Step 1:

HTML content creation is done

### Step 2:

Design of webserver workflow

### Step 3:

Implementation using Python code

### Step 4:

Serving the HTML pages.

### Step 5:

Testing the webserver

## PROGRAM:

```
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
```

## OUTPUT:
###server-side output :
![serverside](https://user-images.githubusercontent.com/119288183/211008864-0742fedd-4de9-4d9a-9874-9ad27d355f75.png)

### client side output:
![Screenshot from 2023-01-06 17-29-57](https://user-images.githubusercontent.com/119288183/211009010-100aff8e-2258-4666-99b8-8f681fbed24c.png)




## RESULT:
The program is executed succesfully
