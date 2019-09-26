from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm

def new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            image = form.cleaned_data.get('image')
            article = Article.objects.create(title=title, content=content)
            return redirect('articles:detail', article.id)
    else:
        form = ArticleForm()
        return render(request, 'new.html', {'form':form})

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
    comments = article.comment_set.all()
    return render(request, 'detail.html', {
        'article':article,
        'comments':comments,
    })

def edit(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    # article = Article.objects.get(id=article_id)
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article.title = form.cleaned_data.get('title')
            article.content = form.cleaned_data.get('content')
            article.image = form.cleaned_data.get('image')
            article.save()
            return redirect('articles:detail', article_id)
    else:
        form = ArticleForm()
        return render(request, 'edit.html', {
            'form':form,
            'article':article,
        })

def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('articles:index')

def comment_create(request, article_id):
    Comment.objects.create(
        content = request.GET.get('content'),
        article = Article.objects.get(id=article_id)
    )
    return redirect('articles:detail', article_id)

def comment_delete(request, article_id, comment_id):
    article = Article.objects.get(id=article_id)
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('articles:detail', article.id)