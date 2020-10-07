from django.contrib import admin
from .models import Review, Comment

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'movie_title', 'created_at', 'updated_at', ]

admin.site.register(Review, ReviewAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', ]

admin.site.register(Comment, CommentAdmin)