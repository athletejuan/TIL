from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content','image']    # {}는 순서가 없어서 title, content, image 입력창의 순서가 일정치 않음

# class ArticleForm(forms.Form):
#     title = forms.CharField(
#         label = '제목',
#         widget = forms.TextInput(attrs={
#             'placeholder':'The title!',
#         })
#     )
#     content = forms.CharField(
#         label = '내용',
#         widget = forms.Textarea(attrs={
#             'class':'input-content',
#             'rows':5,
#             'cols':50,
#             'placeholder':'Fill the content',
#         })
#     )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']