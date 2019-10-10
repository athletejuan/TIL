from django.shortcuts import render, redirect
from django.http import HttpResponse
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
        'number': 10
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