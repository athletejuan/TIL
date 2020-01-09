import requests
from decouple import config
from pprint import pprint as pp

# 기본 설정
token = config('TOKEN')
app_url = f'https://api.telegram.org/bot{token}'

# 응답 내용 저장하기
update_url = f'{app_url}/getUpdates'
response = requests.get(update_url).json()

# chat_id 찾아서 꺼내기
chat_id = response.get('result')[0].get('message').get('chat').get('id')
text = '안녕하세요'

message_url = f'{app_url}/sendMessage?chat_id={chat_id}&text={text}'

print(requests.get(message_url))