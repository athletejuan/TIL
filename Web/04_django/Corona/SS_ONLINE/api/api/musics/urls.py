from django.urls import path
from . import views

app_name = "music"

urlpatterns = [
    path('artists/', views.artists, name="artists"),
    path('artists/<int:artist_pk>/', views.artist_detail, name="artist_detail"),
    path('musics/', views.musics, name="musics"),
    path('musics/<int:music_pk>/', views.music_detail, name="music_detail"),
    path('musics/<int:music_pk>/comments/', views.music_comments, name="music_comments"),
    path('comments/<int:comment_pk>/', views.comment_edit, name="comment_edit"),
]