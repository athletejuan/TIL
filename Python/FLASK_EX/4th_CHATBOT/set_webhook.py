import requests
from decouple import config

token = config('TOKEN')
app_url = f'https://api.telegram.org/bot{token}'
ngrok_url = '###'
python_anywhere_url = 'https://juan.pythonanywhere.com/'

ngrok_setting = f'{app_url}/setWebhook?url={ngrok_url}/telegram'
anywhere_setting = f'{app_url}/setWebhook?url={python_anywhere_url}/telegram'

res = requests.get(anywhere_setting)
# print(res.text)