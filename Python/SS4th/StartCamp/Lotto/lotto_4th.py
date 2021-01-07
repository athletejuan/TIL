import requests
import random

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=874'

res = requests.get(url)
data = res.json()

winner = []

for i in range(1,7):
    winner.append(data[f'drwtNo{i}'])

lotto = sorted(random.sample(range(1,46),6))
match = set(lotto)&set(winner)
rank = len(match)
cnt = 0

while rank < 5:
    lotto = sorted(random.sample(range(1,46),6))
    match = set(lotto)&set(winner)
    rank = len(match)
    cnt += 1
    if rank == 6:
        print("OMG! 1st price!!")
    elif rank == 5:
        print("Awesome! 3rd price!")
    elif rank == 4:
        print("Very Good! 4th grade")
    elif rank == 3:
        print("Not bad. 5th grade")
    else:
        print("WTF!!")
print(cnt)