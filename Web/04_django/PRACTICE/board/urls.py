from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    # path('create/', views.create),
    path('<int:article_id>/', views.show),
    path('<int:article_id>/edit/', views.edit),
    path('<int:article_id>/delete/', views.delete),
]
