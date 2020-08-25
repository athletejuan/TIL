from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST
from .models import Article
from .forms import ArticleForm

def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)


@require_http_methods(['GET', 'POST'])
def new(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article = Article.objects.create(title=title, content=content)
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
    return render(request, 'articles/form.html', context)


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)


@require_http_methods(['GET', 'POST'])
def edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            # article.title = form.cleaned_data.get('title')
            # article.content = form.cleaned_data.get('content')
            # article.save()
            form.save()
        # article.title = request.POST.get('title')
        # article.content = request.POST.get('content')
        # article.save()
            return redirect('articles:detail', article.pk)
    else:
        # form = ArticleForm(instance=article)
        form = ArticleForm(initial=article.__dict__)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/form.html', context)


@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('articles:index')