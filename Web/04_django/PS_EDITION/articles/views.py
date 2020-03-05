from django.shortcuts import render
from .models import Article

def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles':articles})

def new(request):
    return render(request, 'new.html')

def create(request):
    article = Article()
    article.title = request.GET.get('title')
    article.content = request.GET.get('content')
    article.save()
    return render(request, 'create.html')

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'detail.html', {'article':article})