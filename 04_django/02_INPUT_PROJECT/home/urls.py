from django.urls import path
from . import views

# url: /home/
urlpatterns = [
    path('', views.index),
    path('about/', views.about),
]