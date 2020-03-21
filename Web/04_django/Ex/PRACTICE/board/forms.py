from django import forms 
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label = "제목",
        widget = forms.TextInput(attrs={
            'placeholder': 'Enter a Title'
        })
    )
    content = forms.CharField(
        label = "내용",
        widget = forms.Textarea(attrs={
            'class': 'input-content',
            'rows':5,
            'cols':50,
            'placeholder': 'Enter the content',
        })
    )

    class Meta:
        model = Article
        fields = ['title','content','image',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]