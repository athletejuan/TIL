import requests
from bs4 import BeautifulSoup
import random

# url = 'http://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=877'

# url2 = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=877'

# res = requests.get(url2)
# data = res.json()
# real =[]
# for i in range(1,7):
#     real.append(data[f'drwtNo{i}'])

# numbers = range(1,46)
# lotto = sorted(random.sample(numbers, 6))

# print(real)
# print(lotto)



url = 'https://dhlottery.co.kr/common.do?method=main'

res = requests.get(url).text
data = BeautifulSoup(res, 'html.parser')
# selects = data.select_one('#numView')
# print(selects)

winner = []
for i in range(1,7):
    select = data.select_one(f'#numView > #drwtNo{i}').text
    winner.append(int(select))
# print(winner)
# print(','.join(winner))

numbers = range(1,46)
my_nums = sorted(random.sample(numbers, 6))
# print(my_nums)
match = []
for num in my_nums:
    if num in winner:
        match.append(num)
rank = len(match)

count = 0
while rank < 6:
    my_nums = sorted(random.sample(numbers, 6))
    match = []
    count += 1
    for num in my_nums:
        if num in winner:
            match.append(num)
    rank = len(match)
    if rank == 6:
        print('1등')
    elif rank == 5:
        print('3등')
    elif rank == 4:
        print('4등')
    elif rank == 3:
        print('5등')
    else:
        print('꽝!')
    print(count)