from django.shortcuts import render, redirect
from .models import Article

def index(request):
    articles = Article.objects.all()[::-1]
    return render(request, 'index.html', {'articles':articles})

# def new(request):
#     return render(request, 'new.html')

def create(request):
    if request.method == "POST":
        article = Article()
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        # return render(request, 'create.html', {'article':article})
        return redirect(f'/articles/{ article.id }/')
    else:
        return render(request, 'create.html')

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'detail.html', {'article':article})

# def edit(request, article_id):
#     article = Article.objects.get(id=article_id)
#     return render(request, 'edit.html', {'article':article})

def update(request, article_id):
    if request.method == "POST":
        article = Article.objects.get(id=article_id)
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        # return render(request, 'update.html', {'article':article})
        return redirect(f'/articles/{ article.id }/')
    else:
        article = Article.objects.get(id=article_id)
        return render(request, 'edit.html', {'article':article})

def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == "POST":
        article.delete()
    return redirect('/articles/')