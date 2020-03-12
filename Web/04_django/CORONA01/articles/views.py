from django.shortcuts import render, redirect
from .models import Article, Comment

def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles':articles})

# def new(request):
#     return render(request, 'new.html')

def create(request):
    if request.method == "POST":
        article = Article()
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:detail', article.id)
    else:
        return render(request, 'create.html')

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    comments = article.comment_set.all()
    return render(request, 'detail.html', {'article':article, 'comments':comments})

# def edit(request, article_id):
#     article = Article.objects.get(id=article_id)
#     return render(request, 'edit.html', {'article':article})

def update(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == "POST":
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:detail', article.id)
    else:
        return render(request, 'update.html', {'article':article})

def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == "POST":
        article.delete()
    return redirect('articles:index')

def comments_create(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == "POST":
        comment = Comment()
        comment.content = request.POST.get('content')
        comment.article = article
        comment.save()
        return redirect('articles:detail', article.id)
    else:
        return redirect('articles:detail', article.id)

def comments_delete(request, article_id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.method == 'POST':
        comment.delete()
        return redirect('articles:detail', article_id)
    else:
        return redirect('articles:detail', article_id)