from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
# from IPython import embed
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST

def index(request):
    articles = Article.objects.all()[::-1]
    return render(request, 'board/index.html', {
        'articles':articles,
    })

@login_required()
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        # embed() # embed를 쓰고 실행하면 여기에서 동작이 멈춤
        if form.is_valid():     # 유효성 검사
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            # 아래는 form 형식
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article = Article.objects.create(title=title, content=content)

            # 기존 양식
            # article = Article()
            # article.title = request.POST.get('input_title')
            # article.content = request.POST.get('input_content')
            # article.image = request.FILES.get('image')
            # article.save()
            return redirect('board:detail', article.id)
            # return render(request, 'create.html')
    else:
        form = ArticleForm()
    context = {'form': form}
    return render(request, 'board/form.html', context)

def detail(request, article_id):
    # article = Article.objects.get(id=article_id)
    article = get_object_or_404(Article, id=article_id)
    person = get_object_or_404(get_user_model(), id=article.user.id)
    comments = article.comment_set.all()
    comment_form = CommentForm()
    return render(request, 'board/detail.html', {
        'article':article,
        'comments':comments,
        'comment_form':comment_form,
        'person':person,
    })

def delete(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    # article = Article.objects.get(id=article_id)
    if article.user == request.user:    # 작성한 유저와 삭제요청을 한 유저가 같으면 조건문 실행
        if request.method == 'POST':
            article.delete()
            return redirect('board:index')
        else:
            return redirect('board:detail', article.id)
    else:
        return redirect('board:index')

@login_required()
def update(request, article_id):
    # article = Article.objects.get(id=article_id)
    article = get_object_or_404(Article, id=article_id)
    if article.user == request.user:    # 작성한 유저와 삭제요청을 한 유저가 같으면 조건문 실행
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)   # model form 을 사용하기 위해 instance 추가
            if form.is_valid():
                form.save()
                return redirect('board:detail', article.id)
        else:
            form = ArticleForm(instance=article)   # 여기서 마지막 return 으로 간다.
            # article = Article.objects.get(id=article_id)
            # article.title = request.POST.get('input_title')
            # article.content = request.POST.get('input_content')
            # article.save()
    else:
        return redirect('board:index')
    return render(request, 'board/form.html', {
        'form':form,
        'article':article,
    })

@login_required()
@require_POST   # POST 요청이 아닌 요청이 들어오면 404 에러가 뜬다.
def comments_create(request, article_id):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.article_id = article_id
        comment.save()
    return redirect('board:detail', article_id)

@login_required()
@require_POST
def comments_delete(request, article_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.user:
        return redirect('board:detail', article_id)
    comment.delete()
    return redirect('board:detail', article_id)

@login_required()
def like(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.user in article.like_users.all(): # 이 게시글에 좋아요를 누른 유저 중 요청을 한 유저(request.user)가 있다면
        article.like_users.remove(request.user)  # 목록에서 지워준다. (즉 좋아요를 취소 한다는 의미)
    else:
        article.like_users.add(request.user)
    return redirect('board:index')


# 팔로우 : 특정 대상을 팔로우하는 경우 그 대상의 소식을 만날 수 있습니다.
# 팔로워 : 나 또는 특정 대상을 팔로우하는 사람을 뜻합니다.
# 팔로잉 : 나 또는 특정 대상이 팔로우하는 사람을 뜻합니다.
@login_required()
def follow(request, article_id, user_id):
    person = get_object_or_404(get_user_model(), id=user_id)
    if request.user in person.followers.all():
        person.followers.remove(request.user)
    else:
        person.followers.add(request.user)
    return redirect('board:detail', article_id)
