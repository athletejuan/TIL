import requests
from decouple import config

token = config('TOKEN')
app_url = f'https://api.telegram.org/bot{token}'
ngrok_url = '###'

ngrok_setting = f'{app_url}/setWebhook?url={ngrok_url}/telegram'

res = requests.get(ngrok_setting)
# print(res.text)