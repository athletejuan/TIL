from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

def new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
        # article = Article()
        # article.title = request.POST.get('input_title')
        # article.content = request.POST.get('input_content')
        # article.image = request.FILES.get('image)
        # article.save()
            return redirect('board:detail', article.id)
    else:
        form = ArticleForm()
        return render(request, 'form.html', {'form':form})

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
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
        # article.title = request.POST.get('input_title')
        # article.content = request.POST.get('input_content')
        # article.save()
            return redirect('board:detail', article.id)
    else:
        form = ArticleForm(instance=article)
        return render(request, 'form.html', {
            'form':form,
            'article':article,
        })

def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('board:index')