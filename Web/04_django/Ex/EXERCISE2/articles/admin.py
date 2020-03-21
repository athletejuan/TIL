from django.contrib import admin
from articles.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'id','title','user','created_at','updated_at',
    ]

admin.site.register(Article, ArticleAdmin)