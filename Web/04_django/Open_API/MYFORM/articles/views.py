from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

def index(request):
    articles = Article.objects.all()
    return render(request, 'articles/index.html', {'articles':articles})

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            article = Article.objects.create(title=title, content=content)
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
    article = Article.objects.get(pk=article_id)
    return render(request, 'articles/detail.html', {'article':article})