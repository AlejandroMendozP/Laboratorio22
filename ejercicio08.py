from wsgiref.simple_server import make_server
from app07 import app

server = make_server("localhost", 8000, app)
print("Servidor corriendo en http://localhost:8000")
server.serve_forever()