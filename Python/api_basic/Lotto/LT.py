import requests
import random

url = 'http://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=877'

url2 = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=877'

res = requests.get(url2)
data = res.json()
real =[]
for i in range(1,7):
    real.append(data[f'drwtNo{i}'])

numbers = range(1,46)
lotto = sorted(random.sample(numbers, 6))

print(real)
print(lotto)