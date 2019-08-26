from django.shortcuts import render, redirect
from .models import Article    

def new(request):
    if request.method == 'POST':
        article = Article()
        article.title = request.POST.get('input_title')
        article.content = request.POST.get('input_content')
        article.image = request.FILES.get('image')
        article.save()
        return redirect('board:index')
        # return render(request, 'create.html')
    else:
        return render(request, 'new.html')

def index(request):
    articles = Article.objects.all()[::-1]
    return render(request, 'index.html', {
        'articles':articles,
    })

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    # comments = board.comment_set.all()
    return render(request, 'detail.html', {
        'article':article,
        # 'comments':comments
    })

def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == 'POST':
        article.delete()
        return redirect('board:index')
    else:
        return redirect('board:detail', article.id)

def edit(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == 'POST':
        article = Article.objects.get(id=article_id)
        article.title = request.POST.get('input_title')
        article.content = request.POST.get('input_content')
        article.save()
        return redirect('board:detail', article.id)
    else:
        return render(request, 'edit.html', {
            'article':article,
        })    