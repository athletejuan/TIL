from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Article


def index(request):
    articles = Article.objects.all()
    user = request.user
    context = {
        'articles':articles,
        'user':user
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        article = Article()
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:detail', article.pk)
    else:
        return render(request, 'articles/create.html')

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {
        'article':article
    }
    return render(request, 'articles/detail.html', context)

def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:detail', article.pk)
    else:
        context = {
            'article':article
        }
        return render(request, 'articles/update.html', context)

def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('articles:index')

@login_required
def like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    user = request.user
    if article.like_users.filter(pk=user.pk).exists():
        article.like_users.remove(user)
        liked = False
    else:
        article.like_users.add(user)
        liked = True
    context = {
        'liked':liked,
        'count':article.like_users.count(),
    }
    return JsonResponse(context)
    
    # if user in article.like_users.all():
    #     article.like_users.remove(user)
    # else:
    #     article.like_users.add(user)
    # return redirect('articles:index')