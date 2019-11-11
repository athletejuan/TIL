from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.views.decorators.http import require_POST

def index(request):
    articles = Article.objects.all()
    return render(request, 'articles/index.html', {'articles':articles})

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article = Article.objects.create(title=title, content=content)
            return redirect('articles:detail', article.id)
    else:
        form = ArticleForm()
        return render(request, 'articles/form.html', {'form':form})
    #     article = Article()
    #     article.title = request.POST.get('title')
    #     article.content = request.POST.get('content')
    #     article.image = request.FILES.get('image')
    #     article.save()
    #     return redirect('articles:detail', article.pk )
    # else:
    #     return render(request, 'articles/new.html')

def detail(request, article_id):
    # article = Article.objects.get(pk=article_id)
    article = get_object_or_404(Article, pk=article_id)
    comments = article.comment_set.all()
    comment_form = CommentForm()
    return render(request, 'articles/detail.html', {'article':article, 'comments':comments, 'comment_form':comment_form})

@require_POST
def delete(request, article_id):
    # article = Article.objects.get(pk=article_id)
    article = get_object_or_404(Article, pk=article_id)
    # if request.method == 'POST':
    article.delete()
    return redirect('articles:index')
    # return redirect('articles:detail', article.id)

def update(request, article_id):
    # article = Article.objects.get(pk=article_id)
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            # article.title = form.cleaned_data.get('title')
            # article.content = form.cleaned_data.get('content')
            # article.save()
            return redirect('articles:detail', article.id)
    else:
        form = ArticleForm(instance=article)
        # form = ArticleForm(initial=article.__dict__)
    return render(request, 'articles/form.html', {'form':form, 'article':article})

@require_POST
def comment_create(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    # if request.method == "POST":
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        # content = comment_form.cleaned_data.get('content')
        # comment = Comment.objects.create(content=content)
        comment.article = article
        comment.save()
        # comment = Comment()
        # comment.content = request.POST.get('content')
        # comment.article = article
        # comment.save()
    return redirect('articles:detail', article.id)
    
@require_POST
def comment_delete(request, article_id, comment_id):
    # if request.method == "POST":
    # comment = Comment.objects.get(pk=comment_id)
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('articles:detail', article_id)