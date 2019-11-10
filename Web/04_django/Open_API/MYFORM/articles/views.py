from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm

def index(request):
    articles = Article.objects.all()
    return render(request, 'articles/index.html', {'articles':articles})

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article = Article.objects.create(title=title, content=content)
            return redirect('articles:detail', article.id)
    else:
        form = ArticleForm()
        return render(request, 'articles/new.html', {'form':form})
    #     article = Article()
    #     article.title = request.POST.get('title')
    #     article.content = request.POST.get('content')
    #     article.image = request.FILES.get('image')
    #     article.save()
    #     return redirect('articles:detail', article.pk )
    # else:
    #     return render(request, 'articles/new.html')

def detail(request, article_id):
    # article = Article.objects.get(pk=article_id)
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'articles/detail.html', {'article':article})

def delete(request, article_id):
    # article = Article.objects.get(pk=article_id)
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article.id)

def update(request, article_id):
    # article = Article.objects.get(pk=article_id)
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            # article.title = form.cleaned_data.get('title')
            # article.content = form.cleaned_data.get('content')
            # article.save()
            return redirect('articles:detail', article.id)
    else:
        form = ArticleForm(instance=article)
        # form = ArticleForm(initial=article.__dict__)
    return render(request, 'articles/new.html', {'form':form})