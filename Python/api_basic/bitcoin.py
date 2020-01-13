import requests
from pprint import pprint as pp

url = 'https://api.bithumb.com/public/ticker/all'
bithumb = requests.get(url).json()['data']

for key,value in bithumb.items():
    if type(value) == type(dict()):
        now = float(value['closing_price'])
        start = float(value['opening_price'])
        if now - start > 0:
            print(f'{key}: 상승장')
        else:
            print(f'{key}: 하락장')
    else:
        continue