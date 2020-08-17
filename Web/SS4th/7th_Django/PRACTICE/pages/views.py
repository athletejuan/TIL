from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs
import random

def lotto(request):
    # dhlottery main page
    res = requests.get('https://dhlottery.co.kr/common.do?method=main')
    data = bs(res.text)
    count = data.select_one('#lottoDrwNo').text
    lucky = []
    for i in range(1,7):
        lucky.append(int(data.select_one(f'#drwtNo{i}').text))
    bonus = int(data.select_one('#bnusNo').text)

    # json
    jres = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=924')
    jdata = jres.json()
    count = jdata['drwNo']
    lucky = []
    for i in range(1,7):
        lucky.append(jdata[f'drwtNo{i}'])
    bonus = jdata['bnusNo']

    # dhlottery result page
    # res = requests.get('https://dhlottery.co.kr/gameResult.do?method=byWin')
    # data = bs(res.text)
    # count = data.select_one('#article > div:nth-child(2) > div > div.win_result > h4').text
    # nums = data.select('#article > div:nth-child(2) > div > div.win_result > div > div.num.win > p > span')
    # bonus = data.select_one('#article > div:nth-child(2) > div > div.win_result > div > div.num.bonus > p > span').text
    # lucky = []
    # for num in nums:
    #     lucky.append(int(num.text))

    now = {'1등': 0, '2등': 0, '3등': 0, '4등': 0, '5등': 0, '꽝': 0}
    for i in range(1000):
        my = sorted(random.sample(range(1,46), 6))
        if len(set(my) & set(lucky)) == 6:
            now['1등'] += 1
        elif len(set(my) & set(lucky)) == 5 and bonus in my:
            now['2등'] += 1
        elif len(set(my) & set(lucky)) == 5:
            now['3등'] += 1
        elif len(set(my) & set(lucky)) == 4:
            now['4등'] += 1
        elif len(set(my) & set(lucky)) == 3:
            now['5등'] += 1
        else:
            now['꽝'] += 1
    context = {
        'count': count,
        # 'count': count[:3],  # 당첨결과 페이지는 h4태그안에 'OOO회 당첨결과'까지 들어가 있으므로 slicing 필요
        'lucky': lucky,
        'bonus': bonus,
        'now': now,
    }
    return render(request, 'lotto.html', context)