from django.shortcuts import render, HttpResponse
import json

def index(request):
    return HttpResponse('hi django :)')

def about(request):
    me = {
        'name':'juan',
        'role':'intern',
        'e-mail':'juan@hphk.kr',
    }
    return HttpResponse(json.dumps(me))

def portfolio(request):
    return render(request, 'portfolio.html')

def help(request):
    return render(request, 'help.html')