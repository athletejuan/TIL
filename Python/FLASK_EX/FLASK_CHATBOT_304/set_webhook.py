import requests

token = '794763224:AAHsF9_3G9MQfG7TE2l7G3Wv5-ujheNgMNM'
app_url = f'https://api.telegram.org/bot{token}'
ngrok_url = 'https://5931ab47.ngrok.io'
set_webhook_url = f'{app_url}/setWebhook?url={ngrok_url}/telegram'

response = requests.get(set_webhook_url)
print(response.text)
