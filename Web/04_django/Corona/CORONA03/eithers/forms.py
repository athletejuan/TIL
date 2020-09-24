from django import forms
from .models import Question, Comment

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'


class CommentForm(forms.ModelForm):
    SELECT_A = False
    SELECT_B = True
    SELECTS = [
        (SELECT_A, 'BLUE'),
        (SELECT_B, 'RED'),
    ]
    select = forms.ChoiceField(choices=SELECTS, widget=forms.Select())

    class Meta:
        model = Comment
        fields = ['select', 'content']