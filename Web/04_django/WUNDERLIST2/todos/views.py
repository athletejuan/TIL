from django.shortcuts import render, redirect
from .models import Todo

def index(request):
    todos = Todo.objects.all()[::-1]
    context = {
        'todos':todos
    }
    return render(request, 'index.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        due_date = request.POST.get('due-date')
        
        Todo.objects.create(title=title, due_date=due_date)
        return redirect('/todos')