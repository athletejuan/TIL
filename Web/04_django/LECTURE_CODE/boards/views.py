from django.shortcuts import render
from .models import Article

def index(request):
    articles = Article.objects.all()[::-1]
    return render(request, 'index.html', {
        'articles':articles,
    })

def new(request):
    return render(request, 'new.html')

def create(request):
    article = Article()
    article.title = request.GET.get('title')
    article.content = request.GET.get('content')
    article.save()
    return render(request, 'create.html')
    
    # 2nd method
    # title = request.GET.get('title')
    # content = request.GET.get('content')
    # article = Article(title=title, content=content)
    # article.save()

    # 3rd method
    # Article.objects.create(title=title, content=content)

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
    article.title = request.GET.get('title')
    article.content = request.GET.get('content')
    article.save()
    return render(request, 'update.html')

def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    articles = Article.objects.all()[::-1]
    return render(request, 'index.html', {
        'articles':articles
    })