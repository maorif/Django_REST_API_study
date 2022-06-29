import requests

endpoint = 'http://localhost:8000/api/products/create/'
data = {
    # "name": "teclado 2",
    # "description": "teclado mecanico",
    "price": 179.99
}
get_response = requests.post(endpoint, json=data)
print(get_response.json())