from django.shortcuts import render
import random

def lotto(request):
    numbers = sorted(random.sample(range(1,46), 6))
    context = {
        'numbers':numbers
    }
    return render(request, 'lotto.html', context)


def dinner(request, menu, peoples):
    context = {
        'menu': menu,
        'peoples':peoples
    }
    return render(request, 'dinner.html', context)