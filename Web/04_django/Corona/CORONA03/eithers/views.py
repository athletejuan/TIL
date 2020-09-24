from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, Count
from .models import Question, Comment
from .forms import QuestionForm, CommentForm

def main(request):
    questions = Question.objects.order_by('-pk')
    context = {
        'questions': questions
    }
    return render(request, 'eithers/main.html', context)


def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            return redirect('eithers:detail', question.pk)
    else:
        form = QuestionForm()
    context = {
        'form': form
    }
    return render(request, 'eithers/create.html', context)


def detail(request, pk):
    comment_form = CommentForm()
    total_count = Count('comment')
    count_A = Count('comment', filter=Q(comment__select=False))
    count_B = Count('comment', filter=Q(comment__select=True))

    result = Question.objects.annotate(
        total_count=total_count,
        count_A=count_A,
        count_B=count_B,
    )
    question = get_object_or_404(result, pk=pk)
    comments = question.comment_set.order_by('-pk')

    per_A = round(question.count_A / question.total_count * 100, 2) if question.total_count else 0
    per_B = round(question.count_B / question.total_count * 100, 2) if question.total_count else 0

    context = {
        'question': question,
        'comment_form': comment_form,
        'comments': comments,
        'per_A': per_A,
        'per_B': per_B,
    }
    return render(request, 'eithers/detail.html', context)


def comments(request, pk):
    comment_form = CommentForm(request.POST)
    
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.question_id = pk
        comment.save()
        return redirect('eithers:detail', pk)
    context = {
        'comment_form': comment_form,
    }
    return redirect('eithers:detail', pk)