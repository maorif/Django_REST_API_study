import requests

# requests.get() # --> API

# HTTP request --> HTML
# REST Api HTTP request --> JSON ( or xml)

endpoint = 'http://localhost:8000/api/'
endpoint_post = 'http://localhost:8000/api/products/'

get_response = requests.get(endpoint, params={"oi" : 123}, json={"query":"hiho"}) # HTTP request
post_response = requests.post(endpoint_post, json={"name": "celery", "description":"test celery django", "price": 0.00})
# print(get_response.headers)
# print(get_response.text)
print(post_response.json())
