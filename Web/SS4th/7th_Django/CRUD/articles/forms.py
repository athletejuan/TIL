from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    # title = forms.CharField(max_length=30)
    # content = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Article
        fields = '__all__'