from django.shortcuts import render, redirect
from .models import Article

def new(request):
    return render(request, 'board/new.html')

def create(request):
    article = Article()
    article.title = request.GET.get('input_title')
    article.content = request.GET.get('input_content')
    article.save()
    return redirect(f'/board/{article.id}/')

def index(request):
    articles = Article.objects.all()
    return render(request, 'board/index.html', {
        'articles':articles,
    })

def show(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'board/show.html', {
        'article':article,
    })

def edit(request, article_id):
    article = Article.objects.get(pk=article_id)
    context = {
        'article':article,
    }
    return render(request, 'board/edit.html', context)

def update(request, article_id):
    article = Article.objects.get(pk=article_id)
    article.title = request.GET.get('input_title')
    article.content = request.GET.get('input_content')
    article.save()
    return redirect(f'/board/{article.id}/')

def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect ('/board/')