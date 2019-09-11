from django.shortcuts import render
from .models import Todo

def index(request):
    todos = Todo.objects.all()[::-1]
    return render(request, 'index.html',{
        'todos':todos
    })

def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.GET.get('title')
    due_date = request.GET.get('due-date')

    Todo.objects.create(title=title, due_date=due_date)
    return render(request, 'create.html')