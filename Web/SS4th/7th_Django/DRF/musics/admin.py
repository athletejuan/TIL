from django.contrib import admin
from .models import Artist, Music


class ArtistAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(Artist, ArtistAdmin)


class MusicAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'artist', ]

admin.site.register(Music, MusicAdmin)