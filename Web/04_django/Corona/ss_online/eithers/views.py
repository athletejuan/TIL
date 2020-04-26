from django.db.models import Q, Count
from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Comment
from .forms import QuestionForm, CommentForm

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
            return redirect('eithers:index')
    else:
        form = QuestionForm()
    context = {
        'form':form
    }
    return render(request, 'eithers/create.html', context)

def detail(request, question_id):
    result = Question.objects.annotate(
        total_count = Count('comment'),
        count_a = Count('comment', filter=Q(comment__pick=0)),
        # count_a=Count('comment', filter=Q(comment__pick=False)),
        count_b = Count('comment', filter=Q(comment__pick=1)),
        # count_b=Count('comment', filter=Q(comment__pick=True)),
    )
    question = get_object_or_404(result, id=question_id)
    comments = question.comment_set.order_by('-pk')
    comment_form = CommentForm()

    if question.total_count:
        a_part = round(question.count_a / question.total_count *100, 2)
        b_part = round(question.count_b / question.total_count *100, 2)
    else:
        a_part, b_part = 0, 0

    context = {
        'question':question,
        'comments':comments,
        'comment_form':comment_form,
        'a_part':a_part,
        'b_part':b_part,
    }
    return render(request, 'eithers/detail.html', context)

