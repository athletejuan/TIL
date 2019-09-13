from django.shortcuts import render, redirect
from .models import Article

def new(request):
    if request.method == "POST":
        article = Article()
        article.title = request.POST.get('input_title')
        article.content = request.POST.get('input_content')
        article.save()
        return redirect(f'/board/{article.id}/')
    else:
        return render(request, 'board/new.html')

# def create(request):
#     article = Article()
#     article.title = request.GET.get('input_title')
#     article.content = request.GET.get('input_content')
#     article.save()
#     return redirect(f'/board/articles/{article.id}/')

def index(request):
    articles = Article.objects.all()
    return render(request, 'board/index.html', {
        'articles':articles
    })

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'board/detail.html', {
    'article': article,
    })

def edit(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == "POST":
        article.title = request.POST.get('input_title')
        article.content = request.POST.get('input_content')
        article.save()
        return redirect('/board/')
    else:
        return render(request, 'board/edit.html', {
            'article':article
        })

def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('/board/')