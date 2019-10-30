from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.detail),
    path('create/', views.create),
    path('new/', views.new),
    path('', views.index),
]