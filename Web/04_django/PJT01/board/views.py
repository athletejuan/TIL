from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
# from IPython import embed
from .forms import ArticleForm, CommentForm
from django.views.decorators.http import require_POST

def new(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        # embed() # embed를 쓰고 실행하면 여기에서 동작이 멈춤
        if form.is_valid():     # 유효성 검사
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            # 아래는 form양식
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article = Article.objects.create(title=title, content=content)

            # 기존 양식
            # article = Article()
            # article.title = request.POST.get('input_title')
            # article.content = request.POST.get('input_content')
            # article.image = request.FILES.get('image')
            # article.save()
            return redirect('board:index', article.id)
            # return render(request, 'create.html')
    else:
        form = ArticleForm()
    context = {'form': form}
    return render(request, 'form.html', context)

def index(request):
    articles = Article.objects.all()[::-1]
    return render(request, 'index.html', {
        'articles':articles,
    })

def detail(request, article_id):
    # article = Article.objects.get(id=article_id)
    article = get_object_or_404(Article, id=article_id)
    person = get_object_or_404(get_user_model(), id=article.user.id)
    comments = article.comment_set.all()
    comment_form = CommentForm()
    return render(request, 'detail.html', {
        'article':article,
        'comments':comments,
        'comment_form':comment_form,
        'person':person,
    })

def delete(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    # article = Article.objects.get(id=article_id)
    if article.user == request.user:
        if request.method == 'POST':
            article.delete()
            return redirect('board:index')
        else:
            return redirect('board:detail', article.id)
    else:
        return redirect('board:index')

def edit(request, article_id):
    # article = Article.objects.get(id=article_id)
    article = get_object_or_404(Article, id=article_id)
    if article.user == request.user:
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
    return render(request, 'form.html', {
        'form':form,
        'article':article,
    })
@require_POST
def comments_create(request, article_id):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.article_id = article_id
        comment.save()
    return redirect('board:detail', article_id)

@require_POST
def comments_delete(request, article_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.user:
        return redirect('board:detail', article_id)
    comment.delete()
    return redirect('board:detail', article_id)