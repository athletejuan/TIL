from django.shortcuts import render, redirect
from .models import Movie

def index(request):
    movies = Movie.objects.order_by('-pk')
    return render(request, 'movies/index.html', {'movies':movies})

# def new(request):
#     return render(request, 'movies/new.html')

def create(request):
    if request.method == 'POST':
        movie = Movie()
        movie.title = request.POST.get('title')
        movie.title_en = request.POST.get('title_en')
        movie.audience = request.POST.get('audience')
        movie.open_date = request.POST.get('open_date')
        movie.genre = request.POST.get('genre')
        movie.watch_grade = request.POST.get('watch_grade')
        movie.score = request.POST.get('score')
        movie.poster_url = request.POST.get('poster_url')
        movie.description = request.POST.get('description')
        movie.save()
        return redirect('movies:detail', movie.pk)
    else:
        return render(request, 'movies/new.html')

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, 'movies/detail.html', {'movie':movie})

# def edit(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     return render(request, 'movies/edit.html', {'movie':movie})

def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        movie.title = request.POST.get('title')
        movie.title_en = request.POST.get('title_en')
        movie.audience = request.POST.get('audience')
        movie.open_date = request.POST.get('open_date')
        movie.genre = request.POST.get('genre')
        movie.watch_grade = request.POST.get('watch_grade')
        movie.score = request.POST.get('score')
        movie.poster_url = request.POST.get('poster_url')
        movie.description = request.POST.get('description')
        movie.save()
        return redirect('movies:detail', movie.pk)
    else:
        return render(request, 'movies/edit.html', {'movie':movie})

def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:index')
    else:
        return redirect('movies:detail', movie.pk)