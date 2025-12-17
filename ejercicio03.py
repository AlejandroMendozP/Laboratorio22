import requests

url = "https://httpbin.org/get"

response = requests.get(url)

data = response.json()

print("IP:")
print(data["origin"])
print()

print("Headers:")
for clave, valor in data["headers"].items():
    print(f"{clave}: {valor}")
print()

print("Args:")
print(data["args"])