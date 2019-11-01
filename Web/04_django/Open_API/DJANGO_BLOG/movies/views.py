from django.shortcuts import render, redirect
from .models import Movie

def index(request):
    movies = Movie.objects.order_by('-pk')
    return render(request, 'movies/index.html', {'movies':movies})

def new(request):
    return render(request, 'movies/new.html')

def create(request):
    movie = Movie()
    movie.title = request.GET.get('title')
    movie.title_en = request.GET.get('title_en')
    movie.audience = request.GET.get('audience')
    movie.open_date = request.GET.get('open_date')
    movie.genre = request.GET.get('genre')
    movie.watch_grade = request.GET.get('watch_grade')
    movie.score = request.GET.get('score')
    movie.poster_url = request.GET.get('poster_url')
    movie.description = request.GET.get('description')
    movie.save()
    return render(request, 'movies/create.html', {'movie':movie})

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, 'movies/detail.html', {'movie':movie})

def edit(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, 'movies/edit.html', {'movie':movie})

def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.title = request.GET.get('title')
    movie.title_en = request.GET.get('title_en')
    movie.audience = request.GET.get('audience')
    movie.open_date = request.GET.get('open_date')
    movie.genre = request.GET.get('genre')
    movie.watch_grade = request.GET.get('watch_grade')
    movie.score = request.GET.get('score')
    movie.poster_url = request.GET.get('poster_url')
    movie.description = request.GET.get('description')
    movie.save()
    return render(request, 'movies/update.html', {'movie':movie})

def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('/movie/')