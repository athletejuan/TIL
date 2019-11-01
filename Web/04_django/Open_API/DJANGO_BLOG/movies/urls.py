from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/delete/', views.delete),
    path('<int:pk>/update/', views.update),
    path('<int:pk>/edit/', views.edit),
    path('<int:pk>/', views.detail),
    path('create/', views.create),
    path('new/', views.new),
    path('', views.index),
]