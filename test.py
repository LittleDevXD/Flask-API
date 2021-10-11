import requests
import json

# Query
query = "http://127.0.0.1:5000/"

response = requests.get(query + '/home/3')
print(response.json())


