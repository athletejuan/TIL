from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden

def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles':articles
    }
    return render(request, 'articles/index.html', context)

# def new(request):
#     return render(request, 'articles/new.html')

@login_required
def create(request):
    # if request.user.is_authenticated:
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
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

@login_required
def edit(request, article_id):
    article = Article.objects.get(id=article_id)
    # if request.user.is_authenticated:
    if request.user == article.user:
        if request.method == "POST":
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                article = form.save(commit=False)
                article.user = request.user
                article.save()
                return redirect('articles:detail', article.id)
        # article.title = request.POST.get('title')
        # article.content = request.POST.get('content')
        # article.save()
        # return redirect('articles:detail', article.id)
        else:
            form = ArticleForm(instance=article)
    else:
        # error 메시지 보여주고 목록페이지로 이동
        messages.warning(request, '본인 글만 수정 가능합니다.')
        return redirect('articles:index')
        # 403 Error code를 반환
        # return HttpResponseForbidden()
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

@login_required
def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.user == article.user:
        if request.method == "POST":
            article.delete()
    return redirect('articles:index')

@login_required
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
            comment.user = request.user
            comment.save()
    return redirect('articles:detail', article_id)

@login_required
def comments_delete(request, article_id, comment_id):
    # article = Article.objects.get(id=article_id)
    if request.user == comment.user:
        if request.method == "POST":
            comment = Comment.objects.get(id=comment_id)
            comment.delete()
    return redirect('articles:detail', article_id)

@login_required
def like(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if article.like_users.filter(id=request.user.id).exists():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    return redirect('articles:index')