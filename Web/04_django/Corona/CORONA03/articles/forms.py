from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title form-control', 
                'placeholder': 'Enter the title',
                'maxlength': 10,
            }
        ),
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content form-control',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={
            'required': 'Please enter your content'
        }
    )
    class Meta:
        model = Article
        # fields = ['title', 'content', ]
        fields = '__all__'

# class ArticleForm(forms.Form):
#     REGION_A = 'sl'
#     REGION_B = 'dj'
#     REGION_C = 'gj'
#     REGION_D = 'gm'
#     REGIONS = [
#         (REGION_A, '서울'),
#         (REGION_B, '대전'),
#         (REGION_C, '광주'),
#         (REGION_D, '구미'),
#     ]
#     title = forms.CharField(max_length=30)
#     content = forms.CharField(widget=forms.Textarea)
#     region = forms.ChoiceField(choices=REGIONS, widget=forms.RadioSelect())


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ['article', ]