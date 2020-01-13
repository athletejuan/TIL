import random
import requests

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=874'

res = requests.get(url)
data = res.json()
# print(data)

winner = []

for i in range(1,7):
    winner.append(data[f'drwtNo{i}'])

# print(winner)

lotto = sorted(random.sample(range(1,46),6))

match = set(lotto)&set(winner)

cnt = 0
while len(match) < 5:
    lotto = sorted(random.sample(range(1,46),6))
    print(lotto)
    match = set(lotto)&set(winner)  
    cnt += 1
    if len(match) == 6:
        print('OMG! 1st Place!')
    elif len(match) == 5:
        print('Awesome~ 3rd grade')
    elif len(match) == 4:
        print('Excellent, 4th grade')
    elif len(match) == 3:
        print('Good!! 5th grade')
    else:
        print("Don't be disappointed")
print(f'winner number is: {winner}')
print(cnt)