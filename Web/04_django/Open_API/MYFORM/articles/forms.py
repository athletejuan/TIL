from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(
        label = '제목',
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter the title',
        })
    )
    content = forms.CharField(
        label = '내용',
        widget = forms.Textarea(attrs={
            'class':'input-content',
            'rows':5,
            'cols':50,
            'placeholder':'Enter the content',
        })
    )
