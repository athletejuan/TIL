import requests
from decouple import config
from pprint import pprint as pp

# url = 'https://api.telegram.org/bot<token>/METHOD_NAME'

base = 'https://api.telegram.org'
token = config('TOKEN')

url = f'{base}/bot{token}/getUpdates'

res = requests.get(url)
data = res.json()
# pp(data)

# 처음 메시지 보낸 사람에게 응답하기
chat_id = data['result'][0]['message']['chat']['id']
text = "2019.10.18 독립예정일"

url = f'{base}/bot{token}/sendMessage?chat_id={chat_id}&text={text}'

# requests.get(url)
# data = res.json()
# print(data)

# 메시지 보낸 모든 사람에게 응답하기
senders = []
for i in data['result']:
    senders.append(i['message']['chat']['id'])

receivers = set(senders)

for i in receivers:
    url = f'{base}/bot{token}/sendMessage?chat_id={i}&text={text}'
    requests.get(url)