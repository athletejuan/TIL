from django import forms
from .models import Question, Comment

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

class CommentForm(forms.ModelForm):
    # PICK_A = False
    # PICK_B = True
    # PICKS = [
    #     (PICK_A, 'A'),
    #     (PICK_B, 'B'),
    # ]
    # pick = forms.ChoiceField(choices=PICKS, widget=forms.RadioSelect())

    class Meta:
        model = Comment
        fields = ['selecting', 'content',]