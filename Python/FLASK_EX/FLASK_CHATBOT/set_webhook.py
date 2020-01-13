from decouple import config
import requests

token = config('TOKEN')
app_url = f'https://api.telegram.org/bot{token}'
pythonanywhere_url = 'https://###.pythonanywhere.com'
ngrok_url = '###'
# set_webhook_url = f'{app_url}/setWebhook?url={ngrok_url}/telegram'
set_webhook_url = f'{app_url}/setWebhook?url={pythonanywhere_url}/telegram'    # pythonanywhere 배포시

response = requests.get(set_webhook_url)
print(response.text)