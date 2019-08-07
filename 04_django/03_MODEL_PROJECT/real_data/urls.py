from django.urls import path
from . import views

# 'real_data/'
urlpatterns = [
    path('', views.index),
    path('art/', views.art),
    path('output/', views.output),
]