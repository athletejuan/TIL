import requests

token = '###'
app_url = f'https://api.telegram.org/bot{token}'
# ngrok_url = 'https://5931ab47.ngrok.io'
pythonanywhere_url = 'https://juan.pythonanywhere.com'
# set_webhook_url = f'{app_url}/setWebhook?url={ngrok_url}/telegram'
set_webhook_url = f'{app_url}/setWebhook?url={pythonanywhere_url}/telegram'

response = requests.get(set_webhook_url)
print(response.text)
