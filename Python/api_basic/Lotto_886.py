import requests
import random

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=886'

res = requests.get(url)
data = res.json()

lotto_886 = []
for i in range(1,7):
    lotto_886.append(data[f'drwtNo{i}'])

my_num = [3, 15, 19, 23, 34, 45]

match = set(lotto_886) & set(my_num)

if len(match) == 6:
    print('1st place')
elif len(match) == 5:
    print('3rd place')
elif len(match) == 4:
    print('4th place')
elif len(match) == 3:
    print('5th place')
else:
    print('KKwang')