from django.shortcuts import render, redirect
from .models import Todo

def index(request):
    todos = Todo.objects.all()[::-1]
    return render(request, 'index.html',{
        'todos':todos
    })

# def new(request):
#     return render(request, 'new.html')

def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        due_date = request.POST.get('due-date')

        Todo.objects.create(title=title, due_date=due_date)
        return redirect('/todos')
    else:
        return render(request, 'new.html')

# def edit(request, pk):
#     todo = Todo.objects.get(id=pk)
#     return render(request, 'edit.html', {
#         'todo':todo
#     })

def update(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == "POST":
        todo.title = request.POST.get('title')
        todo.due_date = request.POST.get('due-date')
        todo.save()
        return redirect('/todos')
    else:
        return render(request, 'edit.html', {
            'todo':todo
        })

def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/todos')