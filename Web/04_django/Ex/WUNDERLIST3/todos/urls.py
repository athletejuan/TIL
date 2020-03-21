from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.create),
    # path('create/', views.create),
    path('edit/<int:pk>/', views.update),
    # path('update/<int:pk>/', views.update),
    path('delete/<int:pk>/', views.delete),
]