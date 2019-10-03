from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required

# class Article:
#     def __init__(self, title, content, created_at):
#         self.title = title
#         self.content = content
#         self.created_at = created_at

#     def __str__(self):
#         return f'제목: {self.title}, 내용:{self.content}, 작성시간:{self.created_at}'
    
def index(request):    
    # 지금까지 작성된 글을 보여줌    
    articles = Article.objects.order_by('-pk')
    return render(request, 'articles/index.html', {
    'articles': articles,
    })
    
@login_required
def new(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST) # form 객체에 ArticleForm의 형태로 받아온 정보를 입력
        if form.is_valid():     # ArticleForm을 통해 받아온 정보가 형식에 맞는지(유효한지) 확인
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            image_url = request.FILES.get('image')
            user = request.user
            article = Article.objects.create(title=title, content=content, image_url=image_url, user=user)
        # article = Article()
        # article.title = request.POST.get('input_title')
        # article.content = request.POST.get('input_content')
        # article.image_url = request.FILES.get('image')
        # article.user = request.user
        # article.save()
            return redirect('articles:detail', article.id)
    else:
        form = ArticleForm()
        return render(request, 'articles/new.html', {'form':form})

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    comments = article.comment_set.order_by('-id')
    return render(request, 'articles/detail.html', {'article':article, 'comments':comments})

@login_required
def edit(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    # article = Article.objects.get(id=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article.title = form.cleaned_data.get('title')
            article.content = form.cleaned_data.get('content')
            article.image_url = request.FILES.get('image')
            article.user = request.user
            article.save()
        # article.title = request.POST.get('input_title')
        # article.content = request.POST.get('input_content')
        # article.image_url = request.FILES.get('image')
        # article.user = request.user
        # article.save()
            return redirect('articles:detail', article.id)
    else:
        form = ArticleForm(initial=article.__dict__)
    return render(request, 'articles/edit.html', {'form':form, 'article':article}) # image를 form에서 받아오지 않아서인지(?) 'article' 인자가 필요함.

def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('articles:index')

def comments_create(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == 'POST':
        comment = Comment()
        # form에서 보낸 댓글 정보를 저장한다
        comment.content = request.POST.get('content')
        comment.article = article
        comment.save()
        return redirect('articles:detail', article.id)
    else:
        return redirect('articles:detail', article.id)

def comments_delete(request, article_id, comment_id):
    if request.method == 'POST':
        # article = Article.objects.get(id=article_id)
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
        return redirect('articles:detail', article_id)
    else:
        return redirect('articles:detail', article_id)