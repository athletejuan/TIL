import requests
from decouple import config
from pprint import pprint as pp

# telegram_chatbot_url = 'https://api.telegram.org/bot<token>/METHOD_NAME'

base = 'https://api.telegram.org'
token = config('TOKEN')

url = f'{base}/bot{token}/getUpdates'

res = requests.get(url)
data = res.json()
pp(data)

# 처음 메시지 보낸 사람에게 답장하기
chat_id = data['result'][0]['message']['chat']['id']
text = 'you are my No.1'

url = f'{base}/bot{token}/sendMessage?chat_id={chat_id}&text={text}'

requests.get(url)

# 메시지 보낸 모든 사람에게 답장하기(중복 제거)
senders = []
for i in data['result']:
    senders.append(i['message']['chat']['id'])

receivers = set(senders)
text = 'you are my everything'

for i in receivers:
    url = f'{base}/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
    requests.get(url)