import requests

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=874'

res = requests.get(url)

# print(res.text)
# print(res.json())

data = res.json()

winner = []

for i in range(1,7):
    winner.append(data[f'drwtNo{i}'])

print(winner)