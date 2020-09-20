from django.contrib import admin
from .models import Article, Comment

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'image', 'created_at', 'updated_at', ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)