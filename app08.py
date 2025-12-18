import json

estado = {
    "libros": [],
    "contador_id": 1
}

def app(environ, start_response):
    metodo = environ["REQUEST_METHOD"]
    path = environ["PATH_INFO"]

    if metodo == "GET" and path == "/libros":
        start_response("200 OK", [("Content-Type", "application/json")])
        return [json.dumps(estado["libros"]).encode("utf-8")]

    if metodo == "POST" and path == "/libros":
        length = int(environ.get("CONTENT_LENGTH", 0))
        body = environ["wsgi.input"].read(length)
        data = json.loads(body)

        libro = {
            "id": estado["contador_id"],
            "titulo": data["titulo"],
            "autor": data["autor"],
            "anio": data["anio"]
        }

        estado["libros"].append(libro)
        estado["contador_id"] += 1

        start_response("201 Created", [("Content-Type", "application/json")])
        return [json.dumps(libro).encode("utf-8")]

    if metodo == "GET" and path.startswith("/libros/"):
        try:
            libro_id = int(path.split("/")[-1])
        except ValueError:
            start_response("400 Bad Request", [("Content-Type", "text/plain")])
            return [b"ID invalido"]

        for libro in estado["libros"]:
            if libro["id"] == libro_id:
                start_response("200 OK", [("Content-Type", "application/json")])
                return [json.dumps(libro).encode("utf-8")]

        start_response("404 Not Found", [("Content-Type", "text/plain")])
        return [b"Libro no encontrado"]

    start_response("404 Not Found", [("Content-Type", "text/plain")])
    return [b"Ruta no encontrada"]