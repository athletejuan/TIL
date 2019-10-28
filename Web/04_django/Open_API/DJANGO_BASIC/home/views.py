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
    my_lotto = random.sample(numbers, 6)
    # last_lotto = [18, 34, 39, 43, 44, 45]

    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=882'

    res = requests.get(url)
    data = res.json()

    winner = []

    for i in range(1,7):
        winner.append(data[f'drwtNo{i}'])

    match = set(my_lotto) & set(winner)
    rank = len(match)
    cnt = 0

    while rank < 5:
        my_lotto = random.sample(range(1,46),6)
        match = set(my_lotto) & set(winner)
        rank = len(match)
        cnt += 1
    # return HttpResponse(f'오늘의 로또 추천 번호는 {lotto_nums}입니다.')
    return render(request, 'lotto.html', {'my_lotto':my_lotto, 'winner':winner, 'cnt':cnt})

# Variable Routing

def hello(request, name):
    return render(request, 'hello.html', {'name':name})

def introduce(request, name, age):
    return render(request, 'introduce.html', {'name':name, 'age':age})

def square(request, weight, height):
    sq = weight * height
    return render(request, 'square.html', {'weight':weight, 'height':height, 'sq':sq})

# Django Template Language(DTL): from datetime import datetime

def template_language(request):
    menus = ['아메리카노', '카페라떼', '마키아또', '루이보스', '프라푸치노']
    my_sentence = 'Life is short, you need python'
    cafes = ['starbucks', 'coffeebean', 'hollys', 'ediya']
    datetimenow = datetime.now()    # from datetime import datetime 
    empty_list = []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'cafes': cafes,
        'empty_list': empty_list,
        'datetimenow': datetimenow,
    }
    return render(request, 'template_language.html', context)

def image(request):
    return render(request, 'image.html')

def isbirth(request):
    # 6월 27일이면 예, 아니면 아니오
    today = datetime.now()
    if today.month == 6 and today.day == 27:
        result = True
    else:
        result = False
    # context = {'result': result}
    return render(request, 'isbirth.html', {'result': result})

def ispal(request, word):
    if word == word[::-1]:
        result = True
    else:
        result = False
    # context = {'word': word, 'result': result}
    return render(request, 'ispal.html', {'word': word, 'result': result})

# GET / POST

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    message = request.GET.get('message')
    # message2 = request.GET.get('message2')
    context = {
        'message':message,
        # 'message2':message2,
    }
    return render(request, 'catch.html', context)

def word(request):
    return render(request, 'word.html')

def palin(request):
    # ispal2 = request.GET.get('input_word')
    ispal2 = request.GET['input_word']
    if ispal2 == ispal2[::-1]:
        result = True
    else:
        result = False
    return render(request, 'palin.html', {'ispal2':ispal2, 'result':result})

# POST

def user_new(request):
    return render(request, 'user_new.html')

def user_create(request):
    user_name = request.GET.get('name')
    user_password = request.GET.get('pwd')
    # user_name = request.POST.get('name')
    # user_password = request.POST.get('pwd')
    return render(request, 'user_create.html', {'user_name':user_name, 'user_password':user_password})

# Static File

def static_example(request):
    return render(request, 'static_example.html')