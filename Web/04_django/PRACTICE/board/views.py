from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required

def index(request):
    articles = Article.objects.all()
    return render(request, 'board/index.html', {
    'articles':articles,
    })

# def new(request):
#     return render(request, 'board/new.html')

def new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('board:show', article.id)
    else:
        form = ArticleForm()
        return render(request, 'board/form.html', {'form':form})
        
    # if request.method == "POST":
    #     article = Article()
    #     article.title = request.POST.get('input_title')
    #     article.content = request.POST.get('input_content')
    #     article.image = request.FILES.get('image')
    #     article.save()
    #     return redirect('board:show', article.id)
    # else:
    #     return render(request, 'board/new.html')

def show(request, article_id):
    article = Article.objects.get(id=article_id)   
    comments = article.comment_set.order_by('-pk') 
    comment_form = CommentForm()
    return render(request, 'board/show.html', {
    'article':article,
    'comments':comments,
    'comment_form':comment_form,
    })

def edit(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('board:show', article_id)
    else:
        form = ArticleForm(instance=article)
        return render(request, 'board/form.html', {'form':form, 'article':article})
    # if request.method == "POST":
    #     article.title = request.POST.get('input_title')
    #     article.content = request.POST.get('input_content')
    #     article.image = request.FILES.get('image')
    #     article.save()
    #     return redirect('board:show', article_id)
    # else:
    #     return render(request, 'board/edit.html', {'article':article})

def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('board:index')

def comment_create(request, article_id):
    article = Article.objects.get(id=article_id)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
    # comment = Comment()
    # comment.content = request.GET.get('content')
    # comment.article = article
    # comment.save()
    return redirect('board:show', article.id)

def comment_delete(request, article_id, comment_id):
    if request.method == 'POST':
        # article = Article.objects.get(id=article_id)
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
    return redirect('board:show', article_id)

@login_required
def like(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.user in article.like_users.all():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    return redirect('board:index')