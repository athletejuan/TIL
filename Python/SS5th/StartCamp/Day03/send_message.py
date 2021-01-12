import requests

TOKEN = 'TOKEN'
app_url = f'https://api.telegram.org/bot{TOKEN}'

update_url = f'{app_url}/getUpdates'
res = requests.get(update_url).json()

chat_id = res.get('result')[0].get('message').get('chat').get('id')
text = '안녕?'
message_url = f'{app_url}/sendMessage?chat_id={chat_id}&text={text}'
print(requests.get(message_url))