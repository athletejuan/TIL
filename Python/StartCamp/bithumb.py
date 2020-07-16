import requests
from pprint import pprint as pp

url = 'https://api.bithumb.com/public/ticker/all'

res = requests.get(url)
bithumb = res.json()
# print(data)

data = bithumb['data']
for key, value in data.items():
    if key != 'date':
        print(key)
        print(float(value['closing_price'])- float(value['opening_price']))
    