from django.contrib import admin
from boards.models import Article, Comment

class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'id','title','created_at','updated_at',
    ]

admin.site.register(Article, ArticleAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'id','content','created_at','updated_at',
    ]

admin.site.register(Comment, CommentAdmin)