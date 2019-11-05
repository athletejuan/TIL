from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('<int:movie_pk>/scores/<int:score_pk>/delete/', views.score_delete, name='score_delete'),
    path('<int:movie_pk>/scores/new/', views.new, name='new'),
    path('<int:movie_pk>/delete/', views.delete, name='delete'),
    path('<int:movie_pk>/update/', views.update, name='update'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('', views.index, name='index'),
]