from django.shortcuts import render, redirect
from .models import Article

def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles':articles})

# def new(request):
#     return render(request, 'new.html')

def create(request):
    if request.method == 'POST':
        article = Article()
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect(f'/articles/{article.id}/', article.id)
    else:
        return render(request, 'create.html')

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'detail.html', {'article':article})