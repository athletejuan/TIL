from django.shortcuts import render, redirect
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

def edit(request, pk):
    todo = Todo.objects.get(id=pk)
    return render(request, 'edit.html', {
        'todo':todo
    })

def update(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.title = request.GET.get('title')
    todo.due_date = request.GET.get('due-date')
    todo.save()
    return render(request, 'update.html', {
        'todo':todo
    })

def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/todos')