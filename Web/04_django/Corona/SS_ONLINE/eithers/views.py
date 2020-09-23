from django.db.models import Q, Count
from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Comment
from .forms import QuestionForm, CommentForm
from django.views.decorators.http import require_POST
import random

def index(request):
    questions = Question.objects.order_by('-pk')
    context = {
        'questions':questions
    }
    return render(request, 'eithers/index.html', context)

def create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            return redirect('eithers:detail', question.id)
    else:
        form = QuestionForm()
    context = {
        'form':form
    }
    return render(request, 'eithers/create.html', context)

def detail(request, question_pk):
    # result = Question.objects.annotate(
    #     total_count = Count('comment'),
    #     count_a = Count('comment', filter=Q(comment__pick=0)),
    #     # count_a=Count('comment', filter=Q(comment__pick=False)),
    #     count_b = Count('comment', filter=Q(comment__pick=1)),
    #     # count_b=Count('comment', filter=Q(comment__pick=True)),
    # )
    # question = get_object_or_404(result, pk=question_pk)
    # comments = question.comment_set.order_by('-pk')
    # comment_form = CommentForm()

    # if question.total_count:
    #     a_part = round(question.count_a / question.total_count * 100, 2)
    #     b_part = round(question.count_b / question.total_count * 100, 2)
    # else:
    #     a_part, b_part = 0, 0

    # context = {
    #     'question':question,
    #     'comments':comments,
    #     'comment_form':comment_form,
    #     'a_part':a_part,
    #     'b_part':b_part,
    # }
    # return render(request, 'eithers/detail.html', context)
    question = get_object_or_404(Question, pk=question_pk)
    Comment.SELECT[0][1]=question.issue_a
    Comment.SELECT[1][1]=question.issue_b
    comments = question.comment_set.order_by('-pk')
    comment_form = CommentForm()
    count_a = len(question.comment_set.filter(pick=False))
    count_b = len(question.comment_set.filter(pick=True))
    total = count_a + count_b

    if total:
        a_part = round(count_a / total * 100, 2)
        b_part = round(count_b / total * 100, 2)
    else:
        a_part, b_part = 0, 0
    context = {
        'question':question,
        'comments':comments,
        'comment_form':comment_form,
        'count_a':count_a,
        'count_b':count_b,
        'a_part':a_part,
        'b_part':b_part,
    }
    return render(request, 'eithers/detail.html', context)

@require_POST
def comment_create(request, question_pk):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        if comment.selecting == 'A':
            comment.pick = False
        else:
            comment.pick = True
        comment.question_id = question_pk
        comment.save()
    return redirect('eithers:detail', question_pk)
    
def random_issue(request):
    # question = get_object_or_404(Question.objects.order_by('?')[:1])
    question = get_object_or_404(Question, pk=random.choice(range(1, Question.objects.count()+1)))
    Comment.SELECT[0][1]=question.issue_a
    Comment.SELECT[1][1]=question.issue_b
    comments = question.comment_set.order_by('-pk')
    comment_form = CommentForm()
    count_a = len(question.comment_set.filter(pick=False))
    count_b = len(question.comment_set.filter(pick=True))
    total = count_a + count_b

    if total:
        a_part = round(count_a / total * 100, 2)
        b_part = round(count_b / total * 100, 2)
    else:
        a_part, b_part = 0, 0
    context = {
        'question':question,
        'comments':comments,
        'comment_form':comment_form,
        'count_a':count_a,
        'count_b':count_b,
        'a_part':a_part,
        'b_part':b_part,
    }
    return render(request, 'eithers/detail.html', context)