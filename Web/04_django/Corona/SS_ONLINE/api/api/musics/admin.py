from django.contrib import admin
from .models import Artist, Music, Comment

class ArtistAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
admin.site.register(Artist, ArtistAdmin)

class MusicAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
admin.site.register(Music, MusicAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content']
admin.site.register(Comment, CommentAdmin)