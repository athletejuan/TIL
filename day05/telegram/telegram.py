import requests
from decouple import config
from pprint import pprint

base = "https://api.telegram.org"
token = config('TELEGRAM_TOKEN')
method = "getUpdates"

url = f"{base}/{token}/{method}"
res = requests.get(url).json()

chat_id = res['result'][0]['message']['chat']['id']

setWebhook = 'https://api.telegram.org/810810149:AAHxEydh7DeiqdVlIr1kBmszimG64ng1D24/setWebhook?url=https://13c3794d.ngrok.io/810810149:AAHxEydh7DeiqdVlIr1kBmszimG64ng1D24'
deleteWebhook = 'https://api.telegram.org/810810149:AAHxEydh7DeiqdVlIr1kBmszimG64ng1D24/deleteWebhook'