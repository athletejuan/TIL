from django.shortcuts import render, redirect
from .models import Article

def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    article = Article()
    article.title = request.GET.get('title')
    article.content = request.GET.get('content')
    article.save()
    return render(request, 'articles/create.html')

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    context = {
        'article':article
    }
    return render(request, 'articles/detail.html', context)

def edit(request, article_id):
    article = Article.objects.get(id=article_id)
    context = {
        'article':article
    }
    return render(request, 'articles/edit.html', context)

def update(request, article_id):
    article = Article.objects.get(id=article_id)
    article.title = request.GET.get('title')
    article.content = request.GET.get('content')
    article.save()
    return redirect(f'/articles/{ article.id }')

def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('/articles/')