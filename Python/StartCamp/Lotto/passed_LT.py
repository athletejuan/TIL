import requests
import random

# random_lotto = sorted(random.sample(range(1,46),6))
# print(random_lotto)

url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=879"

res = requests.get(url)
data = res.json()
# print(data)

real = []
for i in range(1,7):
    real.append(data[f'drwtNo{i}'])

myfortune = [3, 15, 19, 23, 34, 45]

match = set(real)&set(myfortune)
print(real)
print(myfortune)

cnt = len(match)
# print(f'일치하는 번호 {match}, {cnt}개' )
if cnt == 6:
    print(f'일치하는 번호 {match}, {cnt}개, 즉 대박! 1등')
elif cnt == 5:
    print(f'일치하는 번호 {match}, {cnt}개, 즉 3등')
elif cnt == 4:
    print(f'일치하는 번호 {match}, {cnt}개, 즉 4등')
elif cnt == 3:
    print(f'일치하는 번호 {match}, {cnt}개, 즉 5등')
else:
    print(f'일치하는 번호 {match}, {cnt}개, 즉 꽝!')