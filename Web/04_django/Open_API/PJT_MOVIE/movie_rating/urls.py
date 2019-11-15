from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('<int:movie_id>/ratings/<int:rating_id>/delete/', views.rating_delete, name='rating_delete'),
    path('<int:movie_id>/ratings/new/', views.rating_create, name='rating_create'),
    path('<int:movie_id>/delete/', views.delete, name='delete'),
    path('<int:movie_id>/edit/', views.edit, name='edit'),
    path('<int:movie_id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('', views.index, name='index'),
]