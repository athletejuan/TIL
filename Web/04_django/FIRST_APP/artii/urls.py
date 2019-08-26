from django.urls import path
from . import views

urlpatterns = [
    path('', views.artii),
    path('result/', views.result),
]