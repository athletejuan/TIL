from decouple import config
import requests

token = config('TOKEN')
app_url = f'https://api.telegram.org/bot{token}'
ngrok_url = 'https://be7637c1.ngrok.io'
set_webhook_url = f'{app_url}/setWebhook?url={ngrok_url}/telegram'

response = requests.get(set_webhook_url)
print(response.text)