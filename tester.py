# For testing the Amazon URL validator microservice

import requests

while True:
    amazon_url = input('Please enter a URL to check whether it is a valid Amazon URL or not: ')
    endpoint_url = 'http://127.0.0.1:5000/validate'
    payload = {'URL': amazon_url}

    result = requests.post(url=endpoint_url, json=payload)

    print(result.json())