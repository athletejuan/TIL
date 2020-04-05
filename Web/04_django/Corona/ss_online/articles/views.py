from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request, 'articles/index.html', context)

# def new(request):
#     return render(request, 'articles/new.html')

def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.id)
        # article = Article()
        # article.title = request.POST.get('title')
        # article.content = request.POST.get('content')
        # article.save()
        # return redirect('articles:detail', article.id)
    else:
        form = ArticleForm()
        return render(request, 'articles/new.html', {'form':form})

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    context = {
        'article':article
    }
    return render(request, 'articles/detail.html', context)

def edit(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.id)
        # article.title = request.POST.get('title')
        # article.content = request.POST.get('content')
        # article.save()
        return redirect('articles:detail', article.id)
    else:
        form = ArticleForm(instance=article)
        context = {
            'article':article,
            'form':form,
        }
        return render(request, 'articles/edit.html', context)

# def update(request, article_id):
#     article = Article.objects.get(id=article_id)
#     article.title = request.GET.get('title')
#     article.content = request.GET.get('content')
#     article.save()
#     return redirect(f'/articles/{ article.id }/')

def delete(request, article_id):
    # if request.method == "POST":
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('articles:index')