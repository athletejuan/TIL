from django.shortcuts import render, redirect
from .models import Article, Comment

def index(request):
    articles = Article.objects.all()[::-1]
    return render(request, 'index.html', {
        'articles':articles,
    })

# def new(request):
#     return render(request, 'new.html')

def create(request):
    if request.method == "POST":
        article = Article()
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.image = request.FILES.get('image')
        article.save()
        return redirect('articles:index')
    else:
        return render(request, 'create.html')
    
    # 2nd method
    # title = request.GET.get('title')
    # content = request.GET.get('content')
    # article = Article(title=title, content=content)
    # article.save()

    # 3rd method
    # Article.objects.create(title=title, content=content)

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    comments = article.comment_set.all()[::-1]
    return render(request, 'detail.html', {
        'article':article,
        'comments':comments,
    })

# def edit(request, article_id):
#     article = Article.objects.get(id=article_id)
#     return render(request, 'edit.html', {
#         'article':article,
#     })

def update(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == "POST":
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.image = request.FILES.get('image')
        article.save()
        return redirect('articles:detail', article.id)
    else:
        return render(request, 'update.html', {'article':article})

def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('articles:index')
    
def create_comment(request, article_id):
    # Comment.objects.create(
    #     content = request.GET.get('content'),
    #     article = Article.objects.get(id=article_id)
    # )
    # return redirect('articles:detail', article_id)
    article = Article.objects.get(id=article_id)
    comment = Comment()
    comment.content = request.GET.get('content')
    comment.article = Article.objects.get(id=article_id)
    comment.save()
    return redirect('articles:detail', article.id)

def delete_comment(request, article_id, comment_id):
    article = Article.objects.get(id=article_id)
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('articles:detail', article.id)
