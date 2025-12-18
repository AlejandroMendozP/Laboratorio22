from wsgiref.simple_server import make_server
import json

def app(environ, start_response):
    metodo = environ["REQUEST_METHOD"]
    path = environ["PATH_INFO"]

    if metodo == "GET" and path == "/":
        start_response("200 OK", [("Content-type","text/plain")])
        return [b"Inicio"]
    
    elif metodo == "GET" and path == "/saludo":
        start_response("200 OK", [("Content-type","text/plain")])
        data = {"msg": "Hola mundo desde WSGI"}
        return [b"Hola mundo desde WSGI"]
    
    start_response("404 Not Found", [("Content-Type", "text/plain")])
    return [b"Ruta no encontrada"]

server = make_server("localhost", 8000, app)
print("Servidor WSGI en http://localhost:8000")
server.serve_forever()