from django.shortcuts import render, redirect
from .models import Article

def index(request):
    # articles = Article.objects.all()
    articles = Article.objects.order_by('-id')
    # articles = Article.objects.all()[::-1]
    return render(request, 'articles/index.html', {'articles':articles})

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title=title, content=content)
    article.save()

    # 2.
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 3.
    # Article.objects.create(title=title, content=content)

    # return render(request, 'articles/create.html')
    # return redirect('/articles/')    # import redirect
    return redirect(f'/articles/{article.id}/')

def detail(request, id):
    article = Article.objects.get(pk=id)
    return render(request, 'articles/detail.html', {'article':article})

def delete(request, id):
    article = Article.objects.get(pk=id)
    article.delete()
    return redirect('/articles/')

def edit(request, id):
    article = Article.objects.get(pk=id)
    return render(request, 'articles/edit.html', {'article':article})

def update(request, id):
    article = Article.objects.get(pk=id)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect(f'/articles/{article.id}/')
