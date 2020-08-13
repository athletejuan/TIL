from django.shortcuts import render
import random

def lotto(request):
    numbers = sorted(random.sample(range(1,46), 6))
    context = {
        'numbers':numbers
    }
    return render(request, 'lotto.html', context)