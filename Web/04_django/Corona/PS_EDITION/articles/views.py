from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm


def index(request):
    articles = Article.objects.all()[::-1]
    return render(request, 'articles/index.html', {'articles':articles})

# def new(request):
#     return render(request, 'new.html')

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
        # article = Article()
        # article.title = request.POST.get('title')
        # article.content = request.POST.get('content')
        # article.save()
        # return redirect(f'/articles/{article.id}/', article.id)
    else:
        form = ArticleForm()
    return render(request, 'articles/create.html', {'form':form})

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'articles/detail.html', {'article':article})



@login_required
def like(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    user = request.user
    if article.like_users.filter(id=user.id).exists():
        article.like_users.remove(user)
    else:
        article.like_users.add(user)
    return redirect('articles:index')