import requests

url = "http://localhost:8000"
data = {"a": 5, "b": 3}

print("Enviando datos...")
r = requests.post(url, json=data)

print("Respuesta del servidor:")
print(r.json())