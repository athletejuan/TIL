from django.contrib import admin
from boards.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'id','title','created_at','updated_at',
    ]

admin.site.register(Article, ArticleAdmin)