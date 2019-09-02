from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
# from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST

def index(request):
    articles = Article.objects.all()[::-1]
    return render(request, 'boards/index.html', {
        'articles':articles,
    })

@login_required()
def new(request):
    if request.method == 'POST':
        article = Article()
        article.title = request.POST.get('input_title')
        article.content = request.POST.get('input_content')
        article.save()
        return redirect(f'/boards/{article.id}/')
    else:
        return render(request, 'boards/new.html')

def detail(request, article_id):
    # article = Article.objects.get(id=article_id)
    article = get_object_or_404(Article, id=article_id)
    person = get_object_or_404(get_user_model(), id=article.user.id)
    return render(request, 'boards/detail.html', {
        'article':article,
        'person':person,
    })

@login_required()
def edit(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if article.user == request.user:
        if request.method == 'POST':
            # article = Article.objects.get(id=article_id)
            article.title = request.POST.get('input_title')
            article.content = request.POST.get('input_content')
            article.save()
            return redirect(f'/boards/{article.id}/')
        else:
            article = Article.objects.get(id=article_id)
    else:
        return redirect('/boards/')
    return render(request, 'boards/edit.html', {
        'article':article,
    })
    
def delete(request, article_id):
    # article = Article.objects.get(id=article_id)
    article = get_object_or_404(Article, id=article_id)
    if article.user == request.user:
        if request.method == "POST":
            article.delete()
            return redirect('/boards/')
        else:
            return redirect(f'/boards/{article.id}/')
    else:
        return redirect('/boards/')