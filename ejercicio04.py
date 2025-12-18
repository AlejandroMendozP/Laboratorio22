import requests

for i in range(1,11):
    r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{i}")
    data = r.json()
    print(data["name"])