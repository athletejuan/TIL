from django.shortcuts import render, HttpResponse
import random   # dinner!
import requests    # lotto하기전에 pip install requests
from datetime import datetime   # DTL

def index(request):
    # return HttpResponse("Welcome to Django")
    return render(request, 'home/index.html')

def hola(request):
    # return HttpResponse("Hello my name is Juan")
    return render(request, 'home/hola.html')

# import random
def dinner(request):
    menus = ['피자','치킨','족발','라면']
    dinner = random.choice(menus)
    # return HttpResponse(f'오늘의 저녁메뉴는 {dinner}입니다.')
    return render(request, 'home/dinner.html', {'menus':menus, 'dinner':dinner})

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
    return render(request, 'home/lotto.html', {'my_lotto':my_lotto, 'winner':winner, 'cnt':cnt})

# Variable Routing

def hello(request, name):
    return render(request, 'home/hello.html', {'name':name})

def introduce(request, name, age):
    return render(request, 'home/introduce.html', {'name':name, 'age':age})

def square(request, weight, height):
    sq = weight * height
    return render(request, 'home/square.html', {'weight':weight, 'height':height, 'sq':sq})

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
    return render(request, 'home/template_language.html', context)

def image(request):
    return render(request, 'home/image.html')

def isbirth(request):
    # 6월 27일이면 예, 아니면 아니오
    today = datetime.now()
    if today.month == 6 and today.day == 27:
        result = True
    else:
        result = False
    # context = {'result': result}
    return render(request, 'home/isbirth.html', {'result': result})

def ispal(request, word):
    if word == word[::-1]:
        result = True
    else:
        result = False
    # context = {'word': word, 'result': result}
    return render(request, 'home/ispal.html', {'word': word, 'result': result})

# GET / POST

def throw(request):
    return render(request, 'home/throw.html')

def catch(request):
    message = request.GET.get('message')
    # message2 = request.GET.get('message2')
    context = {
        'message':message,
        # 'message2':message2,
    }
    return render(request, 'home/catch.html', context)

def word(request):
    return render(request, 'word.html')

def palin(request):
    drome = request.GET.get('input_word')
    # drome = request.GET['input_word']
    if drome == drome[::-1]:
        result = True
    else:
        result = False
    return render(request, 'home/palin.html', {'drome':drome, 'result':result})

# POST

def user_new(request):
    return render(request, 'home/user_new.html')

def user_create(request):
    user_name = request.GET.get('name')
    user_password = request.GET.get('pwd')
    # user_name = request.POST.get('name')
    # user_password = request.POST.get('pwd')
    return render(request, 'home/user_create.html', {'user_name':user_name, 'user_password':user_password})

# Static File

def static_example(request):
    return render(request, 'home/static_example.html')

# URL 분리
# django-admin startapp utilities
# home/url.py
# django_basic/url.py: import include / homes - utilities 분리
# home/urls.py, utilities/urls.py 각각 경로 입력

# Template NameSpace
# utilities에 index 함수 설정한 뒤 로드하면 home/index 로드됨
# installed_apps 입력 순서대로 로드되는 것 보여주고(Static도 마찬가지) templates 에 하위폴더 생성
# templates/home에 html파일 다 옮기고 templates/utilities에 html파일 옮김
# 이제 installed_apps 순서 상관없이 해당하는 index.html 파일 로드됨
# static 아래에도 home 폴더 만들고 static_example.html 파일 안에서 로드되는 link tag 들도 경로 변경

# Template Inheritance (Utilities app 에서 합시다)
# base.html파일 만들고 Bootstrap CDN 받아와서 각 위치에 붙여넣고 {% block %} {% endblock %} 만든다.
# templates/utilities/index.html&base.html 파일 만들어서 상속받아쓰기
