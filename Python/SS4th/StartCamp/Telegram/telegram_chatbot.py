import requests
from decouple import config

base = 'https://api.telegram.org'
token = config('TOKEN')

url = f'{base}/bot{token}/getUpdates'

res = requests.get(url)
data = res.json()

# 첫번째로 메시지 보낸 사람에게 답장보내기
chat_id = data['result'][0]['message']['chat']['id']
text = "Don't forget about it"

url = f'{base}/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
requests.get(url)

# 메시지 보낸 모든 사람에게 답장보내기(중복 제거)
senders = []
for sender in data['result']:
    senders.append(sender['message']['chat']['id'])

receivers = set(senders)
text = "Good Job!"

for receiver in receivers:
    url = f'{base}/bot{token}/sendMessage?chat_id={receiver}&text={text}'
    requests.get(url)
return '전송완료'