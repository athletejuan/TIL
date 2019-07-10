# lotto api를 통해 최신 당첨 번호를 가져온다

import requests
import random

url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866"
res = requests.get(url)
# json 파일 -> python dictionary
# json_lotto = res.text
dict_lotto = res.json()

# winner에 1등 당첨번호 넣기

winner=[]
for i in range(1,7):
    winner.append(dict_lotto[f'drwtNo{i}'])    

# lotto 랜덤 추천
your_lotto = sorted(random.sample(range(1,46),6))

print(winner)
print(your_lotto)

# match=[]
# for i in your_lotto:    
#     for j in winner:
#         if i == j:
#             match.append(i)
# if len(match) == 6:
#     print('1등')
# elif len(match) == 5:
#     print('3등')
# elif len(match) == 4:
#     print('4등')
# elif len(match) == 3:
#     print('5등')
# else:
#     print('꽝')

count = 0

count = len(set(winner) & set(your_lotto))
print(count)
# for w in winner:
#     for y in your_lotto:
#         if w == y:
#             count += 1
# if count == 6:
#     print("1등")
# elif count == 5:
#     print("3등")   
# elif count == 4:
#     print('4등')
# elif count == 3:
#     print('5등')
# else:
#     print('꽝')

trial = 0
while True:
    if count == 6:
        print("1등입니다.")
        break
    trial +=1
    print(trial)
