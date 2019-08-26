from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.index),
    path('articles/new/', views.new),
    path('articles/create/', views.create),
    path('articles/<int:article_id>/', views.show),
    path('articles/<int:article_id>/delete/', views.delete),    
]