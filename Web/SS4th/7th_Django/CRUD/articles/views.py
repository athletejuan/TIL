from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Article
from .forms import ArticleForm

def index(request):
    # articles = Article.objects.all()[::-1]    # 파이썬이 변경
    articles = Article.objects.order_by('-pk')  # DB에서 변경
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)


# def new(request):
#     return render(request, 'articles/new.html')


@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
        # article = Article()
        # article.title = request.POST.get('title')
        # article.content = request.POST.get('content')
        # article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/create.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     context = {
#         'article': article
#     }
#     return render(request, 'articles/edit.html', context)


@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save()
            # article.title = request.POST.get('title')
            # article.content = request.POST.get('content')
            # article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form
    }
    return render(request, 'articles/update.html', context)


@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    # if request.method == 'POST':
    article.delete()
    return redirect('articles:index')
    # else:
    #     return redirect('articles:detail', article.pk)