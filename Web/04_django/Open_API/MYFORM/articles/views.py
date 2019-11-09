from django.shortcuts import render, redirect
from .models import Article

def index(request):
    articles = Article.objects.all()
    return render(request, 'articles/index.html', {'articles':articles})

def create(request):
    if request.method == 'POST':
        article = Article()
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.image = request.FILES.get('image')
        article.save()
        return redirect('articles:detail', article.pk )
    else:
        return render(request, 'articles/new.html')

def detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, 'articles/detail.html', {'article':article})