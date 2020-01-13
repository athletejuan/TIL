import requests
import random

nth = 880
url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={nth}'

res = requests.get(url)
data = res.json()

winner = []
for i in range(1,7):
    winner.append(data[f'drwtNo{i}'])

my_num = [3, 15, 19, 23, 34, 45] 

nums = range(1,46)
random_lotto = sorted(random.sample(nums, 6))

# match = set(winner) & set(random_lotto)
match = set(winner) & set(my_num)
print(winner)
print(my_num)
print(len(match))
# while len(match) < 4:
#     nums = range(1,46)
#     random_lotto = sorted(random.sample(nums, 6))
#     match = set(winner) & set(random_lotto)
#     if len(match) == 6:
#         print("1st")
#     elif len(match) == 5:
#         print('3rd')
#     elif len(match) == 4:
#         print('4th')
#     elif len(match) == 3:
#         print('5th')
#     else:
#         print('Bomb')