from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

def index(request):
    articles = Article.objects.all()[::-1]
    return render(request, 'articles/index.html', {'articles':articles})

# def new(request):
#     return render(request, 'new.html')

def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # image = request.FILES.get('image')
            # article = Article.objects.create(title=title, content=content, image=image)
        # article = Article
        # article.title = request.POST.get('title')
        # article.content = request.POST.get('content')
        # article.image = request.FILES.get('image')
        # article.save()
        # return render(request, 'create.html', {'article':article})
            return redirect('articles:detail', article.id)
    else:
        form = ArticleForm()
        return render(request, 'articles/form.html', {'form':form})

def detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = article.comment_set.order_by('-id')
    comment_form = CommentForm()
    context = {
        'article':article, 
        'comments':comments,
        'comment_form':comment_form,
        }
    return render(request, 'articles/detail.html', context)

# def edit(request, article_id):
#     article = Article.objects.get(id=article_id)
#     return render(request, 'edit.html', {'article':article})

def update(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save()
            # article.title = form.cleaned_data.get('title')
            # article.content = form.cleaned_data.get('content')
            # article.image = request.FILES.get('image')
            # article.save()
        # article.title = request.POST.get('title')
        # article.content = request.POST.get('content')
        # article.image = request.FILES.get('image')
        # article.save()
        # return render(request, 'update.html', {'article':article})
            return redirect('articles:detail', article.id)
    else:
        form = ArticleForm(instance=article)
        return render(request, 'articles/form.html', {'article':article, 'form':form})

def delete(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == "POST":
        article.delete()
    return redirect('articles:index')

def comment_create(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == "POST":
        comment = Comment()
        comment.content = request.POST.get('content')
        comment.article = article
        comment.save()
    return redirect('articles:detail', article.id)

def comment_delete(request, article_id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.method == "POST":
        comment.delete()
    return redirect('articles:detail', article_id)