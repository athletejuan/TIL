from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.views.decorators.http import require_POST

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
    comments = article.comment_set.order_by('-pk')
    comment_form = CommentForm()
    context = {
        'article':article,
        'comments':comments,
        'comment_form':comment_form,
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

@require_POST
def delete(request, article_id):
    # if request.method == "POST":
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('articles:index')

def comments_create(request, article_id):
    # article = Article.objects.get(id=article_id)
    # Comment.objects.create(
    #     content = request.POST.get('content'),
    #     article = article
    # )
    # return redirect('articles:detail', article_id)
    article = Article.objects.get(id=article_id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()
    return redirect('articles:detail', article_id)

def comments_delete(request, article_id, comment_id):
    # article = Article.objects.get(id=article_id)
    if request.method == "POST":
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
    return redirect('articles:detail', article_id)