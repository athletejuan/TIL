from django.shortcuts import render, redirect
from .models import Article, Comment

def new(request):
    if request.method == "POST":
        article = Article()
        article.title = request.POST.get('input_title')
        article.content = request.POST.get('input_content')
        article.save()
        return redirect(f'/articles/{article.id}/')
    else:
        return render(request, 'new.html')

# def create(request):
#     article = Article()
#     article.title = request.GET.get('input_title')
#     article.content = request.GET.get('input_content')
#     article.save()
#     return redirect(f'/articles/{article.id}/')

def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {
        'articles':articles,
    })

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    comments = article.comment_set.all()[::-1]
    return render(request, 'detail.html', {
        'article':article,
        'comments':comments,
    })

def edit(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == "POST":
        article.title = request.POST.get('input_title')
        article.content = request.POST.get('input_content')
        article.save()
        return redirect('/articles/')
    else:
        return render(request, 'edit.html', {
            'article':article
        })

def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('/articles/')

def create_comment(request, article_id):
    Comment.objects.create(
        content = request.GET.get('content'),
        article = Article.objects.get(id=article_id)
    )
    return redirect('articles:detail', article_id)