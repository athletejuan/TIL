from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm

def index(request):
    articles = Article.objects.order_by('-pk')
    context = {'articles':articles}
    return render(request, 'boards/index.html', context)

# def new(request):
#     return render(request, 'new.html')

@login_required
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
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
    # article = Article.objects.get(id=article_id)
    comments = article.comment_set.order_by('-pk')
    context = {
        'article':article,
        'comments':comments,
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
    # article = Article.objects.get(id=article_id)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            # article.title = form.cleaned_data.get('title')
            # article.content = form.cleaned_data.get('content')
            # article.save()
            return redirect('articles:detail', article.id)
    else:
        form = ArticleForm(instance=article)
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
    if request.method == "POST":
        article = get_object_or_404(Article, id=article_id)
        # article = Article.objects.get(id=article_id)
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:index')
    
def comment_create(request, article_id):
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

def comment_delete(request, article_id, comment_id):
    article = Article.objects.get(id=article_id)
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('articles:detail', article.id)
