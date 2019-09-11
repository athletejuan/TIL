import requests
from decouple import config
from pprint import pprint as pp

# url = 'https://api.telegram.org/bot<token>/METHOD_NAME'

base = 'https://api.telegram.org'
token = config('TOKEN')

url = f'{base}/{token}/getUpdates'

res = requests.get(url)
data = res.json()
# pp(data)

chat_id = data['result'][0]['message']['chat']['id']
text = 'ToDo List'

url = f'{base}/{token}/sendMessage?chat_id={chat_id}&text={text}'

requests.get(url)
