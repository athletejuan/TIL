from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

def new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            image = request.FILES.get('image')
            article = Article.objects.create(title=title, content=content, image=image)
        # article = Article()
        # article.title = request.POST.get('input_title')
        # article.content = request.POST.get('input_content')
        # article.save()
            return redirect('board:detail', article.id)
    else:
        form = ArticleForm()
        return render(request, 'new.html', {'form':form})

# def create(request):
#     article = Article()
#     article.title = request.GET.get('input_title')
#     article.content = request.GET.get('input_content')
#     article.save()
#     return redirect(f'/board/{article.id}/')

def index(request):
    articles = Article.objects.order_by('-id')
    return render(request, 'index.html', {
        'articles':articles,
    })

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'detail.html', {
        'article':article,
    })

def edit(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article.title = form.cleaned_data.get('title')
            article.content = form.cleaned_data.get('content')
            article.image = request.FILES.get('image')
            article.save()
        # article.title = request.POST.get('input_title')
        # article.content = request.POST.get('input_content')
        # article.save()
            return redirect('board:detail', article.id)
    else:
        form = ArticleForm(initial=article.__dict__)
        return render(request, 'edit.html', {
            'form':form,
            'article':article,
        })

def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('board:index')