import requests
import random

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=878'

res = requests.get(url)
data = res.json()

winner = []
for i in range(1,7):
    winner.append(data[f'drwtNo{i}'])
print(winner)

nums = range(1,46)
lotto = sorted(random.sample(nums, 6))
myfortune = [3, 15, 19, 23, 34, 45]
print(myfortune)

# match = set(winner)&set(myfortune)
match = set(winner)&set(lotto)

cnt = len(match)

if cnt == 6:
    print('대박! 1등')
elif cnt == 5:
    print('3등')
elif cnt == 4:
    print('4등')
elif cnt == 3:
    print('5등')
else:
    print('꽝')