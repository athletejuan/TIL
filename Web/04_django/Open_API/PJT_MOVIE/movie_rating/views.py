from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Rating
from .forms import MovieForm, RatingForm
from django.views.decorators.http import require_POST

def index(request):
    movies = Movie.objects.all()
    ratings = Rating.objects.order_by('-pk')
    score = 0
    for rating in ratings:
        score += rating.score
    score_div = score / len(ratings)
    return render(request, 'movies/index.html', {'movies':movies, 'score_div':score_div})

def new(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            # movie = form.save()
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:index')
        # movie.title = request.POST.get('title')
        # movie.description = request.POST.get('description')
        # movie.poster = request.FILES.get('poster')
        # movie.save()
    else:
        form = MovieForm()
        return render(request, 'movies/form.html', {'form':form})

def detail(request, movie_id):
    # movie = Movie.objects.get(pk=movie_id)
    movie = get_object_or_404(Movie, pk=movie_id)
    ratings = Rating.objects.order_by('-pk')
    rating_form = RatingForm()
    score = 0
    for rating in ratings:
        score += rating.score
    score_div = score / len(ratings)
    return render(request, 'movies/detail.html', {'movie':movie, 'ratings':ratings, 'rating_form':rating_form, 'score_div':score_div})

def edit(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.id)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies/form.html', {'form':form, 'movie':movie})

@require_POST
def delete(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    movie.delete()
    return redirect('movies:index')
    
@require_POST
def rating_create(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    rating_form = RatingForm(request.POST)
    if rating_form.is_valid():
        rating = rating_form.save(commit=False)
        rating.movie = movie
        rating.user = request.user
        rating.save()
    return redirect('movies:detail', movie_id)
    
@require_POST
def rating_delete(request, movie_id, rating_id):
    rating = get_object_or_404(Rating, pk=rating_id)
    rating.delete()
    return redirect('movies:detail', movie_id)