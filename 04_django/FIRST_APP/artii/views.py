from django.shortcuts import render
import requests

def artii(request):
    return render(request, 'artii/artii.html')

def result(request):
    # 1. 단어를 받아온다.
    word = request.GET.get('word')
    # 2. artii api를 통해 ascii art 결과들을 요청하고,
    url = 'http://artii.herokuapp.com/make?text='
    result = requests.get(url + word).text
    # 3. 결과를 받아와 보여준다.
    context = {
        'word':word,
        'result':result,
    }
    return render(request, 'artii/result.html', context)

