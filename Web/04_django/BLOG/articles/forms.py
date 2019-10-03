from django import forms
from .models import Article, Comment

class ArticleForm(forms.Form):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(attrs={
            'placeholder': "Enter a Title"
        })
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(attrs={
            'class':'input-content',
            'rows':5,
            'cols':50,
            'placeholder':'Enter the Content',
        })
    )
    class Meta:
        model = Article
        fields = ['title','content',]

class CommentForm(forms.Form):
    class Meta:
        model = Comment
        fields = ['content',]
