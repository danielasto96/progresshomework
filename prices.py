import requests
import json

params = dict(
    description='Oracle SE (BYOL), db.t3.medium reserved instance applied'
)

url = 'https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonRDS/20201203195321/us-west-1/index.json'
responce = requests.get(url,params)
json_data = responce.json()
print(json_data)

substring='db.t3'
string = responce.text
if substring in string:
     print('True')
else:
     print('false')
