import requests

product_id = input("Type the product id to be deleted: \n")

try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} is not a valid id')

if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete"

    get_response = requests.delete(endpoint)
    print(get_response.status_code, get_response.status_code==204)

    get_list_endpoint = "http://localhost:8000/api/products/"
    get_list_response = requests.get(get_list_endpoint)
    print(get_list_response.json())