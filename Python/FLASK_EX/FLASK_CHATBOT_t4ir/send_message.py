import requests
from decouple import config

base = 'https://api.telegram.org'
token = config('TOKEN')
chat_id = config('CHAT_ID')
text = 'pythonanywhere deployment'

send_message = requests.get(f'{base}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

print(send_message.text)