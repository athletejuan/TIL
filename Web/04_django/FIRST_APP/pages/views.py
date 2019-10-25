from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup as bs
import random
import datetime

def index(request):
    return render(request, 'pages/index.html')

def home(request):
    # return HttpResponse('HoMePAge')
    name = 'juan'
    data = ['A','B','C']
    empty_data = ['엄복동', '클레멘타인', '성냥팔이소녀의 재림']
    matrix = [[1,2,3],[4,5,6]]
    context = { 
        'name': name,
        'data': data,
        'empty_data': empty_data,
        'matrix': matrix,
        'number': 10,
        'datetime': datetime,
    }
    return render(request, 'pages/home.html', context)

def lotto(request):
    lotto = sorted(random.sample(range(1,46), 6))
    context = {'lotto':lotto,
        'number': 11
    }
    return render(request, 'pages/lotto.html', context)

def cube(request, num):
    cube = num ** 3
    context = {
        'cube':cube,
    }
    return render(request, 'pages/cube.html', context)

def match(request):
    chemi = random.randint(50, 100)
    me = request.POST.get('me')
    you = request.POST.get('you')
    test = request.method
    context = {
        'me': me,
        'you': you,
        'chemi': chemi,
        'test': test,
    }
    return render(request, 'pages/match.html', context)

def dtl(request):
    my_list = ['짜장면','탕수육','짬뽕','양장피']
    select = random.choice(my_list)
    messages = ['apple','banana','cocumber','mango','watermelon','kiwi']
    empty_list = []

    return render(request, 'pages/dtl.html', {'my_list':my_list, 'select':select, 'messages':messages, 'empty_list':empty_list})

def static_example(request):
    return render(request, 'pages/static_example.html')

def bootstrap_example(request):
    return render(request, 'pages/bootstrap_example.html')

def exchange(request):
    url = 'https://finance.naver.com/marketindex/'
    res = requests.get(url).text
    soup = bs(res, 'html.parser')
    ex = soup.select_one('#content > div.NE\=a\:t1k > div._tracklist_mytrack.tracklist_table.tracklist_type1 > table')
    print(f'원/달러 환율은: {ex.text}원 입니다.')
    return render(request, 'pages/ex.html', {'ex':ex.text})

def kospi(request):
    url = 'https://finance.naver.com/sise/'
    res = requests.get(url).text
    soup = bs(res, 'html.parser')
    kospi = soup.select_one('#KOSPI_now')
    # print(f'원/달러 환율은: {kospi.text}원 입니다.')
    return render(request, 'pages/kospi.html', {'kospi':kospi.text})
