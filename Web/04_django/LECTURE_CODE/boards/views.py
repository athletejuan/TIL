from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST

def index(request):
    articles = Article.objects.order_by('-pk')
    context = {'articles':articles}
    return render(request, 'boards/index.html', context)

# def new(request):
#     return render(request, 'new.html')

@login_required
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES) # image 업로드를 위해 request.FILES 추가, update 함수에도.
        if form.is_valid():
            article = form.save(commit=False)
            # article.image = request.FILES.get('image')
            article.user = request.user
            article.save()
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article = Article.objects.create(title=title, content=content)
            return redirect('articles:detail', article.id)
    else:
        form = ArticleForm()
        return render(request, 'boards/form.html', {'form':form})

# def create(request):
#     if request.method == "POST":
#         article = Article()
#         article.title = request.POST.get('title')
#         article.content = request.POST.get('content')
#         article.image = request.FILES.get('image')
#         article.save()
#         return redirect('articles:index')
#     else:
#         return render(request, 'create.html')
    
    # 2nd method
    # title = request.GET.get('title')
    # content = request.GET.get('content')
    # article = Article(title=title, content=content)
    # article.save()

    # 3rd method
    # Article.objects.create(title=title, content=content)

def detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    person = get_object_or_404(get_user_model(), id=article.user.id)
    # article = Article.objects.get(id=article_id)
    comments = article.comment_set.order_by('-pk')
    comment_form = CommentForm()
    context = {
        'article':article,
        'comments':comments,
        'comment_form':comment_form,
        'person':person,
    }
    return render(request, 'boards/detail.html', context)

# def edit(request, article_id):
#     article = Article.objects.get(id=article_id)
#     return render(request, 'edit.html', {
#         'article':article,
#     })

@login_required
def update(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if article.user == request.user:
    # article = Article.objects.get(id=article_id)
        if request.method == "POST":
            form = ArticleForm(request.POST, request.FILES, instance=article)   # request.FILES 추가
            if form.is_valid():
                article = form.save(commit=False)
                # article.image = request.FILES.get('image')
                article.user = request.user
                article.save()
                # article.title = form.cleaned_data.get('title')
                # article.content = form.cleaned_data.get('content')
                # article.save()
                return redirect('articles:detail', article.id)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
        # form = ArticleForm(initial=article.__dict__)
    return render(request, 'boards/form.html', {'form':form,'article':article})

# def update(request, article_id):
#     article = Article.objects.get(id=article_id)
#     if request.method == "POST":
#         article.title = request.POST.get('title')
#         article.content = request.POST.get('content')
#         article.image = request.FILES.get('image')
#         article.save()
#         return redirect('articles:detail', article.id)
#     else:
#         context = {
#             'article':article,
#         }
#         return render(request, 'update.html', context)

def delete(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if article.user == request.user:
        if request.method == "POST":
            # article = Article.objects.get(id=article_id)
            article.delete()
            return redirect('articles:index')
        else:
            return redirect('articles:detail', article.id)
    else:
        return redirect('articles:index')

@login_required
@require_POST   # POST 요청이 아닌 요청이 들어오면 405에러를 보여준다
def comment_create(request, article_id):
    # Comment.objects.create(
    #     content = request.GET.get('content'),
    #     article = Article.objects.get(id=article_id)
    # )
    # return redirect('articles:detail', article_id)
    article = Article.objects.get(id=article_id)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
    # comment = Comment()
    # comment.content = request.POST.get('content')
    # comment.article = Article.objects.get(id=article_id)
    # comment.user = request.user
    # comment.save()
    return redirect('articles:detail', article.id)

@login_required
# @require_POST     # request.user가 comment.user인 경우에만 삭제 버튼이 보이게 하고 이 버튼은 GET요청으로 보내도록 함(댓글과 삭제버튼 a태그로 한줄표시하려고)
def comment_delete(request, article_id, comment_id):
    article = Article.objects.get(id=article_id)
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('articles:detail', article.id)

@login_required
def like(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    user = request.user
    if article.like_users.filter(id=user.id).exists(): # 좋아요를 누른 사람이 이미 좋아요 한 경우
        article.like_users.remove(user) # 좋아요 취소
    else:
        article.like_users.add(user)
    return redirect('articles:index')

# 팔로우 : 특정 대상을 팔로우하는 경우 그 대상의 소식을 만날 수 있습니다.
# 팔로워 : 나 또는 특정 대상을 팔로우하는 사람
# 팔로잉 : 나 또는 특정 대상이 팔로우하는 사람
@login_required
def follow(request, article_id, user_id):
    person = get_object_or_404(get_user_model(), id=user_id)
    if request.user in person.followers.all():
        person.followers.remove(request.user)
    else:
        person.followers.add(request.user)
    return redirect('articles:detail', article_id)