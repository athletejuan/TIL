from django.shortcuts import render, redirect
from .models import Article

def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {
        'articles':articles,
    })

def new(request):
    if request.method == 'POST':
        article = Article()
        article.title = request.POST.get('input_title')
        article.content = request.POST.get('input_content')
        article.save()
        return redirect(f'/boards/{article.id}/')
    else:
        return render(request, 'new.html')

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'detail.html', {
        'article':article,
    })

def edit(request, article_id):
    if request.method == 'POST':
        article = Article.objects.get(id=article_id)
        article.title = request.POST.get('input_title')
        article.content = request.POST.get('input_content')
        article.save()
        return redirect(f'/boards/{article.id}/')
    else:
        article = Article.objects.get(id=article_id)
        return render(request, 'edit.html', {
            'article':article,
        })
    
def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('/boards/')
