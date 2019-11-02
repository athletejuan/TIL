from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST

@login_required
def new(request):
    if request.method == 'POST':
        article = Article()
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.user = request.user
        article.save()
        return redirect('articles:show', article.id)
    else:
        return render(request, 'board/new.html')

def index(request):
    articles = Article.objects.all()
    return render(request, 'board/index.html', {
        'articles': articles,
    })

def show(request, article_id):
    article = Article.objects.get(id=article_id)
    comments = article.comment_set.all()
    person = get_object_or_404(get_user_model(), id=article.user.id)
    return render(request, 'board/show.html', {
        'article': article,
        'comments': comments,
        'person': person,
    })

@login_required
def edit(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:show', article.id)
    else:
        return render(request, 'board/edit.html', {'article':article})

def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect ('articles:index')


def comment_create(request, article_id):
    article = Article.objects.get(pk=article_id)
    if request.method == 'POST':
        comment = Comment()
        comment.content = request.POST.get('content')
        comment.article = article
        comment.save()
        return redirect('articles:show', article.id)
    else:
        return redirect('articles:show', article.id)

def comment_delete(request, article_id, comment_id):
    if request.method == 'POST':
        comment = Comment.objects.get(pk=comment_id)
        comment.delete()
        return redirect('articles:show', article_id)
    else:
        return redirect('articles:show', article_id)

def like(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    user = request.user
    if article.like_users.filter(id=user.id).exists():
        article.like_users.remove(user)
    else:
        article.like_users.add(user)
    return redirect('articles:index')

@login_required
def follow(request, article_id, user_id):
    person = get_object_or_404(get_user_model(), id=user_id)
    if request.user in person.followers.all():
        person.followers.remove(request.user)
    else:
        person.followers.add(request.user)
    return redirect('articles:show', article_id)
