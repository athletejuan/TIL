from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
    path('edit/<int:pk>/', views.edit),
    path('update/<int:pk>/', views.update),
    path('delete/<int:pk>/', views.delete),
]