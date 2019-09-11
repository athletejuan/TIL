from django.shortcuts import render, redirect
from .models import Todo

def index(request):
    todos = Todo.objects.all()[::-1]
    context = {
        'todos':todos
    }
    return render(request, 'todos/index.html', context)

# def new(request):
#     return render(request, 'todos/new.html')

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due-date')

        Todo.objects.create(title=title, due_date=due_date)
        return redirect('todos:index')
    else:
        return render(request, 'todos/new.html')

def edit(request, pk):
    todo = Todo.objects.get(id=pk)
    context = {
        'todo':todo
    }
    return render(request, 'todos/edit.html', context)

def update(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due-date')
        
        
        todo.title = title
        todo.due_date = due_date
        todo.save()
        return redirect('todos:index')
    else:
        todo = Todo.objects.get(id=pk)
        context = {
            'todo':todo
        }
        return render(request, 'todos/edit.html', context)

def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('todos:index')