from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('<int:article_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('', views.index, name='index'),
]