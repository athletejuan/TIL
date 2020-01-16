import requests
from pprint import pprint as pp

token = '###'
app_url = f'https://api.telegram.org/bot{token}'

update_url = f'{app_url}/getUpdates'
response = requests.get(update_url).json()

chat_id = response.get('result')[0].get('message').get('chat').get('id')
text = '테스트2'

message_url = f'{app_url}/sendMessage?chat_id={chat_id}&text={text}'
requests.get(message_url)