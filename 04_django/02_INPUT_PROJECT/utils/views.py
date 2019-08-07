from django.shortcuts import render, redirect
from art import *

def index(request):
    return render(request, 'utils/index.html')

def art(request):
    fonts = ['3d_diagnoal','acrobatic', 'avatar','cards']
    return render(request, 'utils/art.html', {
        'fonts':fonts,
    })

def output(request):
    user_input = request.GET.get('user-input')
    user_font = request.GET.get('user-font')

    if user_input:        
        result = text2art(user_input, font=user_font)                        
        return render(request, 'utils/output.html', {
                'result': result
            })
    else:
        return redirect('/utils/art/')

def throw(request):
    return render(request, 'utils/throw.html')

def catch(request):
    user_input = request.GET.get('user-input')
    return render(request, 'utils/catch.html', {
        'user_input': user_input
    })