from django.shortcuts import render, redirect
from .models import Article
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
    articles = Article.objects.all()
    return render(request, 'articles/index.html', {
    'articles': articles,
    })
    
@login_required
def new(request):
    if request.method == 'POST':
        article = Article()
        article.title = request.POST.get('input_title')
        article.content = request.POST.get('input_content')
        article.img_url = request.POST.get('img_url')
        article.user = request.user
        article.save()
        return redirect('articles:index')
    else:
        return render(request, 'articles/new.html')

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'articles/detail.html', {'article':article})

def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('articles:index')