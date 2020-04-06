from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from .forms import ReviewForm

def review_list(request):
    reviews = Review.objects.all()
    context = {
        'reviews':reviews
    }
    return render(request, 'reviews/review_list.html', context)

def new_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect('community:review_detail', review.pk)
    else:
        form = ReviewForm()
        context = {
            'form':form
        }
        return render(request, 'reviews/new_review.html', context)

# def review_create(request):
#     review = Review()
#     review.title = request.GET.get('title')
#     review.content = request.GET.get('content')
#     review.rank = request.GET.get('rank')
#     review.save()
#     return redirect('/community/')

def review_detail(request, review_id):
    # review = Review.objects.get(id=review_id)
    review = get_object_or_404(Review, id=review_id)
    context = {
        'review':review
    }
    return render(request, 'reviews/review_detail.html', context)