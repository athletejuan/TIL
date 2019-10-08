from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required

@login_required
def new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # image = form.cleaned_data.get('image')
            # article = Article.objects.create(title=title, content=content)
            return redirect('articles:detail', article.id)
    else:
        form = ArticleForm()
        return render(request, 'articles/form.html', {'form':form})

# def create(request):
#     article = Article()
#     article.title = request.GET.get('input_title')
#     article.content = request.GET.get('input_content')
#     article.save()
#     return redirect(f'/articles/{article.id}/')

def index(request):
    articles = Article.objects.all()
    return render(request, 'articles/index.html', {
        'articles':articles,
    })

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    comments = article.comment_set.all()
    return render(request, 'articles/detail.html', {
        'article':article,
        'comments':comments,
    })

@login_required
def edit(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    # article = Article.objects.get(id=article_id)
    if article.user == request.user:
        if request.method == "POST":
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                article = form.save()
                # article.title = form.cleaned_data.get('title')
                # article.content = form.cleaned_data.get('content')
                # article.image = form.cleaned_data.get('image')
                # article.save()
                return redirect('articles:detail', article_id)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    return render(request, 'articles/form.html', {
        'form':form,
        'article':article,
    })

def delete(request, article_id):
    # article = Article.objects.get(id=article_id)
    article = get_object_or_404(Article, id=article_id)
    if request.user == article.user:
        if request.method=='POST':
            article.delete()
            return redirect('articles:index')
        # else:
        #     return redirect('articles:detail', article.id)
    else:
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

@login_required
def like(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    user = request.user
    if article.like_users.filter(id=user.id).exists(): # 해당 게시글을 좋아요 한 유저의 목록 중 해당 유저의 아이디가 존재할 시
        article.like_users.remove(user)  # 좋아요 취소
    else:
        article.like_users.add(user) # 좋아요 추가
    return redirect('articles:index')
