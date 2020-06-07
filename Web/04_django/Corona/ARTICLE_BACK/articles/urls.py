from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    # path('', views.article_list, name="article_list")
]