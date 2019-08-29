from django.shortcuts import render, redirect
from .models import Article

def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {
        'articles':articles,
    })

def new(request):
    return render(request, 'new.html')

def create(request):
    article = Article()
    article.title = request.GET.get('input_title')
    article.content = request.GET.get('input_content')
    article.save()
    return render(request, 'create.html', {
        'article':article,
    })

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'detail.html', {
        'article':article,
    })

def edit(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'edit.html', {
        'article':article,
    })

def update(request, article_id):
    article = Article.objects.get(id=article_id)
    article.title = request.GET.get('input_title')
    article.content = request.GET.get('input_content')
    article.save()
    return render(request, 'update.html', {
        'article':article,
    })
    
def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('/boards/')
