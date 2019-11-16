from django.contrib import admin
from .models import Movie, Rating

class MovieAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','poster','created_at','updated_at']

admin.site.register(Movie, MovieAdmin)

class RatingAdmin(admin.ModelAdmin):
    list_display = ['id','score','content','created_at','updated_at']

admin.site.register(Rating, RatingAdmin)