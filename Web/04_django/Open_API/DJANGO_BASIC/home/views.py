from django.shortcuts import render, HttpResponse
import random   # dinner!
import requests    # lotto하기전에 pip install requests
from datetime import datetime   # DTL

def index(request):
    # return HttpResponse("Welcome to Django")
    return render(request, 'index.html')

def hola(request):
    # return HttpResponse("Hello my name is Juan")
    return render(request, 'hola.html')

# import random
def dinner(request):
    menus = ['피자','치킨','족발','라면']
    dinner = random.choice(menus)
    # return HttpResponse(f'오늘의 저녁메뉴는 {dinner}입니다.')
    return render(request, 'dinner.html', {'menus':menus, 'dinner':dinner})

# import requests
def lotto(request):
    numbers = range(1,46)
    lotto_nums = random.sample(numbers, 6)
    # last_lotto = [18, 34, 39, 43, 44, 45]

    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=882'

    res = requests.get(url)
    data = res.json()

    winner = []

    for i in range(1,7):
        winner.append(data[f'drwtNo{i}'])

    match = set(lotto_nums) & set(winner)
    rank = len(match)
    cnt = 0

    while rank < 5:
        lotto_nums = random.sample(range(1,46),6)
        match = set(lotto_nums) & set(winner)
        rank = len(match)
        cnt += 1
    # return HttpResponse(f'오늘의 로또 추천 번호는 {lotto_nums}입니다.')
    return render(request, 'lotto.html', {'lotto_nums':lotto_nums, 'winner':winner, 'cnt':cnt})

def hello(request, name):
    return render(request, 'hello.html', {'name':name})

def square(request, weight, height):
    sq = weight * height
    return render(request, 'square.html', {'weight':weight, 'height':height, 'sq':sq})

# Django Template Language(DTL): from datetime import datetime

def template_language(request):
    menus = ['아메리카노', '카페라떼', '마키아또', '루이보스', '프라푸치노']
    my_sentence = 'Life is short, you need python'
    cafe = ['starbucks', 'coffeebean', 'hollys', 'ediya']
    datetimenow = datetime.now()    # from datetime import datetime 
    empty_list = []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'cafe': cafe,
        'empty_list': empty_list,
        'datetimenow': datetimenow,
    }
    return render(request, 'template_language.html', context)

def image(request):
    return render(request, 'image.html')

def ispal(request, word):
    if word == word[::-1]:
        result = True
    else:
        result = False
    context = {'word': word, 'result': result}
    return render(request, 'ispal.html', context)

def word(request):
    return render(request, 'word.html')

def palin(request):
    ispal2 = request.GET.get('input_word')
    if ispal2 == ispal2[::-1]:
        result = True
    else:
        result = False
    return render(request, 'palin.html', {'ispal2':ispal2, 'result':result})