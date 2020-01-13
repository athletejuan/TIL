import requests
from pprint import pprint as pp

url = 'https://api.bithumb.com/public/ticker/all'
bithumb = requests.get(url).json()['data']
pp(bithumb)

for key,value in bithumb.items():
    if type(value) == type(dict()):
        now = float(value['closing_price'])
        prev_closing = float(value['prev_closing_price'])
        if now - prev_closing > 0:
            print(f'{key}: 상승장')
        elif now - prev_closing < 0:
            print(f'{key}: 하락장')
        else:
            print(f'{key}: 변동없음')
    else:
        continue