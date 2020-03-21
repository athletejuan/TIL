from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST

def index(request):
    articles = Article.objects.all()[::-1]
    return render(request, 'boards/index.html', {
        'articles':articles,
    })

@login_required()
def new(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect(f'/boards/{article.id}/')
    else:
        form = ArticleForm()
    context = {'form':form}
    return render(request, 'boards/new.html', context)
    # if request.method == 'POST':
    #     article = Article()
    #     article.title = request.POST.get('input_title')
    #     article.content = request.POST.get('input_content')
    #     article.save()
    #     return redirect(f'/boards/{article.id}/')
    # else:
    #     return render(request, 'boards/new.html')

def detail(request, article_id):
    # article = Article.objects.get(id=article_id)
    article = get_object_or_404(Article, id=article_id)
    comments = article.comment_set.order_by('-pk')
    person = get_object_or_404(get_user_model(), id=article.user.id)
    return render(request, 'boards/detail.html', {
        'article':article,
        'comments':comments,
        'person':person,
    })

@login_required()
def edit(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if article.user == request.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                form.save()
            # article = Article.objects.get(id=article_id)
            # article.title = request.POST.get('input_title')
            # article.content = request.POST.get('input_content')
            # article.save()
                return redirect(f'/boards/{article.id}/')
        else:
            # article = Article.objects.get(id=article_id)
            form = ArticleForm(instance=article)
    else:
        return redirect('/boards/')
    return render(request, 'boards/edit.html', {
        'form':form,
        'article':article,
    })
    
def delete(request, article_id):
    # article = Article.objects.get(id=article_id)
    article = get_object_or_404(Article, id=article_id)
    if article.user == request.user:
        if request.method == "POST":
            article.delete()
            return redirect('/boards/')
        else:
            return redirect(f'/boards/{article.id}/')
    else:
        return redirect('/boards/')

def comment_create(request, article_id):
    if request.method == 'POST':
        comment = Comment()
        content = request.POST.get('content')
        article = Article.objects.get(id=article_id)
        user = request.user
        Comment.objects.create(content=content, article=article, user=user)
        return redirect('boards:detail', article_id)
    else:
        return redirect('boards:detail', article_id)

def comment_delete(request, article_id, comment_id):
    # if request.method == 'POST':
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('boards:detail', article_id)
    # else:
    #     return redirect('boards:detail', article_id)