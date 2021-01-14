import requests
from datetime import datetime

today = datetime.now()
start = datetime(2021, 1, 15)
td = today - start
text = f'{td.days + 1}일'

TOKEN = 'TOKEN'
CHAT_ID = 'CHAT_ID'

url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
response = requests.get(url).json()
CHAT_ID = response['result'][0]['message']['chat']['id']

url = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}'
requests.get(url)