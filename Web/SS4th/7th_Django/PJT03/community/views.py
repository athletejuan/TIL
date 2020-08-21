from django.shortcuts import render, redirect
from .models import Review

def review_list(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews
    }
    return render(request, 'community/review_list.html', context)


def new_review(request):
    if request.method == 'POST':
        review = Review()
        review.title = request.POST.get('title')
        review.content = request.POST.get('content')
        review.rank = request.POST.get('rank')
        review.save()
        return redirect('community:review_detail', review.pk)
    else:
        return render(request, 'community/new_review.html')


def review_detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        'review': review
    }
    return render(request, 'community/review_detail.html', context)


def review_edit(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == 'POST':
        review.title = request.POST.get('title')
        review.content = request.POST.get('content')
        review.rannk = request.POST.get('rank')
        review.save()
        return redirect('community:review_detail', review.pk)
    else:
        context = {
            'review': review
        }
        return render(request, 'community/review_edit.html', context)


def review_delete(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == 'POST':
        review.delete()
    return redirect('community:review_list')