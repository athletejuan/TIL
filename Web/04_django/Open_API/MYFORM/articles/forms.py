from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content',]


# class ArticleForm(forms.Form):
#     title = forms.CharField(
#         label = '제목',
#         widget=forms.TextInput(attrs={
#             'placeholder': 'Enter the title',
#         })
#     )
#     content = forms.CharField(
#         label = '내용',
#         widget = forms.Textarea(attrs={
#             'class':'input-content',
#             'rows':5,
#             'cols':50,
#             'placeholder':'Enter the content',
#         })
#     )

class CommentForm(forms.ModelForm):
    # content = forms.CharField()
    class Meta:
        model = Comment
        fields = ['content',]