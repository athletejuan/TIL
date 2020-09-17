from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from IPython import embed
from .models import Review
from .forms import ReviewForm

def review_list(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews
    }
    return render(request, 'community/review_list.html', context)


def create(request):
    # embed()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form
    }
    return render(request, 'community/form.html', context)


def detail(request, review_pk):
    # review = Review.objects.get(pk=review_pk)
    review = get_object_or_404(Review, pk=review_pk)
    context = {
        'review': review
    }
    return render(request, 'community/detail.html', context)


def update(request, review_pk):
    # review = Review.objects.get(pk=review_pk)
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm(instance=review)
    context = {
        'review': review,
        'form': form
    }
    return render(request, 'community/form.html', context)


@require_POST
def delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    review.delete()
    return redirect('community:review_list')