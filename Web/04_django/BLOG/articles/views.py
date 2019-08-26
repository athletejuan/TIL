from django.shortcuts import render, redirect
from datetime import datetime
from .models import Article

blogs = []

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
    return render(request, 'index.html', {
    'articles': articles,
    })

def new(request):
    return render(request, 'new.html')

def create(request):
    article = Article()
    article.title = request.GET.get('input_title')
    article.content = request.GET.get('input_content')
    article.img_url = request.GET.get('img_url')
    article.save()
    return redirect('/')