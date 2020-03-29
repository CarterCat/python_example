# wsgi

# app

def app(environ, start_response):
    start_response('200 ok', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']


# server

from wsgiref.simple_server import make_server

httpd = make_server('', 8000, app)

print("server http on port 8000...")

httpd.serve_forever()


