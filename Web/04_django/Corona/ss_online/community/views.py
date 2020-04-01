from django.shortcuts import render, redirect
from .models import Review

def review_list(request):
    reviews = Review.objects.all()
    context = {
        'reviews':reviews
    }
    return render(request, 'reviews/review_list.html', context)

def new_review(request):
    return render(request, 'reviews/new_review.html')

def review_create(request):
    review = Review()
    review.title = request.GET.get('title')
    review.content = request.GET.get('content')
    review.rank = request.GET.get('rank')
    review.save()
    return redirect('/community/')

def review_detail(request, review_id):
    review = Review.objects.get(id=review_id)
    context = {
        'review':review
    }
    return render(request, 'reviews/review_detail.html', context)