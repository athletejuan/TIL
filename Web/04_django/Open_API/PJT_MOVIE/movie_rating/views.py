from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Rating
from .forms import MovieForm, RatingForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

def index(request):
    movies = Movie.objects.all()
    movie_score ={}
    for movie in movies:
        ratings = movie.rating_set.all()
        if ratings:
            score_sum = 0
            # scores = []
            for rating in ratings:
                score_sum += rating.score
            scores = score_sum / len(ratings)
            movie_score[movie.title] = scores
            # scores.append(score_sum / len(ratings))
        else:
            movie_score[movie.title] = 0
            # scores.append(0)
    # return render(request, 'movies/index.html', {'movies':movies, 'scores':scores})
    return render(request, 'movies/index.html', {'movie_score':movie_score})

@login_required
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
    ratings = movie.rating_set.order_by('-pk')
    rating_form = RatingForm()
    if ratings:
        score_sum = 0
        for rating in ratings:
            score_sum += rating.score
        score = score_sum / len(ratings)
    else:
        score = 0
    return render(request, 'movies/detail.html', {'movie':movie, 'ratings':ratings, 'rating_form':rating_form, 'score':score})

@login_required
def edit(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.user == movie.user:
        if request.method == 'POST':
            form = MovieForm(request.POST, request.FILES, instance=movie)
            if form.is_valid():
                movie = form.save()
                return redirect('movies:detail', movie.id)
        else:
            form = MovieForm(instance=movie)
    else:
        return redirect('movies:detail', movie.id)
    return render(request, 'movies/form.html', {'form':form, 'movie':movie})

@login_required
@require_POST
def delete(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.user == movie.user:
        movie.delete()
    return redirect('movies:index')
    
@login_required
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
    
@login_required
@require_POST
def rating_delete(request, movie_id, rating_id):
    rating = get_object_or_404(Rating, pk=rating_id)
    if request.user == rating.user:
        rating.delete()
    return redirect('movies:detail', movie_id)