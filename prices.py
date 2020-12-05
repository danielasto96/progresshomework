import requests
import json
import sys
print(sys.argv)

url = 'https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonRDS/20201203195321/us-west-1/index.json'
responce = requests.get(url)
json_data = responce.json()
#print(json_data['publicationDate'])
#print(json_data['products'])

#print(json_data.values())
#print(json_data)
#for p_id, p_info in json_data.items():
#    print("\nField:", p_id)

 #   for key in p_info:
 #        print(key + ':', p_info[key])

#print ('20201203195321' in json_data.values())
#print ('offerCode' in json_data['products'])



from nested_lookup import nested_lookup
#print(nested_lookup('products',json_data))

results = nested_lookup(
    key = 'description',
    document = json_data,
    wild = True
)

#print(results)

#from nested_lookup import get_occurrences_and_values

#result = get_occurrences_and_values(json_data, value='db.m4.xlarge')

#print(result)

substring='db.r5.xl'
string = results
if substring in string:
     print('db.t3 is found')
else:
     print('db.t3 is not found')

print(type(results))

#list(filter(lambda x:'db.r5' in x, results))

found = []
for name in results:
    if 'db.t3' in name:
       found.append(name)
print (found)
