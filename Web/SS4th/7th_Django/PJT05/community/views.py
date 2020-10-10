from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.template.defaulttags import register
from django.template.library import Library
from .models import Review, Comment
from .forms import ReviewForm, CommentForm

def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews
    }
    return render(request, 'community/review_list.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form
    }
    return render(request, 'community/form.html', context)


# template로 dictionary 넘겨주고 그 안에서 특정 키값에 해당하는 밸류값을 반환하고자 할때
@register.filter
def get_item(reviews, key):
    return reviews.get(key)


def detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment_form = CommentForm()
    comments = review.comment_set.order_by('-pk')
    context = {
        'review': review,
        'comment_form': comment_form,
        'comments': comments
    }
    return render(request, 'community/review_detail.html', context)


def update(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('community:detail', review_pk)
    else:
        form = ReviewForm(instance=review)
    context = {
        'form': form,
        'review': review,
    }
    return render(request, 'community/form.html', context)


@login_required
def delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'POST':
        review.delete()
        return redirect('community:index')
    return redirect('community:detail', review_pk)


@require_POST
def comment_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
    return redirect('community:detail', review_pk)


@login_required
def like(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'POST':
        if review.like_user.filter(pk=request.user.pk).exists():
            review.like_user.remove(request.user)
        else:
            review.like_user.add(request.user)
    return redirect('community:detail', review.pk)
