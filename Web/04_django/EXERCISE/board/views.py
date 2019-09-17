from django.shortcuts import render, redirect
from .models import Article, Comment

def create(request):
    if request.method == "POST":
        article = Article()
        article.title = request.POST.get('input_title')
        article.content = request.POST.get('input_content')
        article.image = request.FILES.get('image')
        article.save()
        return redirect(f'/board/{article.id}/')
    else:
        return render(request, 'board/create.html')

# def create(request):
#     article = Article()
#     article.title = request.GET.get('input_title')
#     article.content = request.GET.get('input_content')
#     article.save()
#     return redirect(f'/board/articles/{article.id}/')

def index(request):
    articles = Article.objects.all()
    return render(request, 'board/index.html', {
        # 'articles':reversed(articles)
        'articles':articles
    })

def detail(request, article_id):
    # pk라는 id를 가진 글을 찾아와 보여줌
    article = Article.objects.get(id=article_id)
    
    # 해당 글에 달려있는 모든 댓글을 보여줌
    comments = article.comment_set.all()[::-1]
    
    context = {
        'article':article,
        'comments':comments,
        # 'num_of_comments':comments.count,
    }
    return render(request, 'board/detail.html', context)

def update(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == "POST":
        article.title = request.POST.get('input_title')
        article.content = request.POST.get('input_content')
        article.image = request.FILES.get('image')
        article.save()
        return redirect('/board/')
    else:
        return render(request, 'board/update.html', {
            'article':article
        })

def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('/board/')

def create_comment(request, article_id):
    # 댓글 작성, 디테일 페이지로 리다이렉트
    Comment.objects.create(
        content=request.GET.get('content'),
        article=Article.objects.get(id=article_id)
    )
    return redirect('board:detail', article_id)
