from django.shortcuts import render, redirect
from .models import Article

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
        article.save()
        return redirect('/boards/')
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
    return render(request, 'detail.html', {
        'article':article,
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
        article.save()
        return redirect(f'/boards/{article.id}/')
    else:
        return render(request, 'update.html', {'article':article})

def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('/boards/')