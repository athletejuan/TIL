from django import forms
from .models import Question, Comment

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        # fields = '__all__'
        exclude = ['user',]


class CommentForm(forms.ModelForm):
    CHOICES = [
        ['Blue', False],
        ['Red', True],
    ]
    select = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Comment
        fields = ['select', 'content']