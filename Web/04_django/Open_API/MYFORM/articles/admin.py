from django.contrib import admin
from .models import Article, Comment

class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'id','title','content','created_at','updated_at',
    ]

admin.site.register(Article, ArticleAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'pk','content', 'created_at',
    ]
admin.site.register(Comment, CommentAdmin)