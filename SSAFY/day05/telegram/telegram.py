import requests
from decouple import config
from pprint import pprint

base = "https://api.telegram.org"
token = config('TELEGRAM_TOKEN')
method = "getUpdates"

url = f"{base}/{token}/{method}"
res = requests.get(url).json()

chat_id = res['result'][0]['message']['chat']['id']
