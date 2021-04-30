from django.contrib import admin
from .models import Movie, Review, Comment

class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'overview', 'release_date', 'poster_path']

admin.site.register(Movie, MovieAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'rank', 'movie']

admin.site.register(Review, ReviewAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'created_at', 'updated_at', 'review']

admin.site.register(Comment, CommentAdmin)