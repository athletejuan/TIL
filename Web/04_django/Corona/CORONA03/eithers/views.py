from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, Count
from django.views.decorators.http import require_POST
from .models import Question, Comment
from .forms import QuestionForm, CommentForm
import random

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
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('eithers:detail', question.pk)
    else:
        form = QuestionForm()
    context = {
        'form': form
    }
    return render(request, 'eithers/create.html', context)


def detail(request, pk):
    question = Question.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = question.comment_set.order_by('-pk')

    comment_form.CHOICES[0][1] = question.select_A
    comment_form.CHOICES[1][1] = question.select_B
    count_A = len(question.comment_set.filter(pick=False))
    count_B = len(question.comment_set.filter(pick=True))
    total = count_A + count_B

    if total:
        part_A = round(count_A / total * 100, 2)
        part_B = round(count_B / total * 100, 2)
    else:
        part_A, part_B = 0, 0
    # total_count = Count('comment')
    # count_A = Count('comment', filter=Q(comment__select=False))
    # count_B = Count('comment', filter=Q(comment__select=True))

    # result = Question.objects.annotate(
    #     total_count=total_count,
    #     count_A=count_A,
    #     count_B=count_B,
    # )
    # question = get_object_or_404(result, pk=pk)
    # comments = question.comment_set.order_by('-pk')

    # per_A = round(question.count_A / question.total_count * 100, 2) if question.total_count else 0
    # per_B = round(question.count_B / question.total_count * 100, 2) if question.total_count else 0

    context = {
        'question': question,
        'comment_form': comment_form,
        'comments': comments,
        'count_A': count_A,
        'count_B': count_B,
        'part_A': part_A,
        'part_B': part_B,
    }
    return render(request, 'eithers/detail.html', context)


def comments(request, pk):
    comment_form = CommentForm(request.POST)
    
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.question_id = pk
        if comment.select == 'Blue':
            comment.pick = False
        else:
            comment.pick = True
        comment.save()
        return redirect('eithers:detail', pk)
    context = {
        'comment_form': comment_form,
    }
    return redirect('eithers:detail', pk)


def random_question(request):
    q_num = random.choice(range(len(Question.objects.all())))
    # question = Question.objects.get(pk=q_num)
    question = Question.objects.all()[q_num]
    comment_form = CommentForm()
    comments = question.comment_set.order_by('-pk')

    comment_form.CHOICES[0][1] = question.select_A
    comment_form.CHOICES[1][1] = question.select_B
    count_A = len(question.comment_set.filter(pick=False))
    count_B = len(question.comment_set.filter(pick=True))
    total = count_A + count_B

    if total:
        part_A = round(count_A / total * 100, 2)
        part_B = round(count_B / total * 100, 2)
    else:
        part_A, part_B = 0, 0
    
    context = {
        'question': question,
        'comment_form': comment_form,
        'comments': comments,
        'count_A': count_A,
        'count_B': count_B,
        'part_A': part_A,
        'part_B': part_B,
    }
    return render(request, 'eithers/detail.html', context)


@require_POST
def delete(request, pk):
    question = get_object_or_404(Question, pk=pk)
    question.delete()
    return redirect('eithers:main')