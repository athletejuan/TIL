from django.shortcuts import render, redirect
from .models import Genre, Movie, Score

def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies':movies})

def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    scores = movie.score_set.order_by('-pk')
    return render(request, 'movies/detail.html', {'movie':movie, 'scores':scores})

def update(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'POST':
        movie.title = request.POST.get('title')
        movie.audience = request.POST.get('audience')
        movie.poster_url = request.POST.get('poster_url')
        movie.description = request.POST.get('description')
        movie.save()
        return redirect('movies:detail', movie.pk)
    else:
        return render(request, 'movies/edit.html', {'movie':movie})

def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:index')
    else:
        return redirect('movies:detail', movie.pk)

def score_new(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'POST':
        score = Score()
        score.content = request.POST.get('content')
        score.score = request.POST.get('score')
        score.movie = movie
        score.save()
    return redirect('movies:detail', movie.pk)

def score_delete(request, movie_pk, score_pk):
    # movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'POST':
        score = Score.objects.get(pk=score_pk)
        score.delete()
    return redirect('movies:detail', movie_pk)