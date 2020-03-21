from django.urls import path
from articles import views

urlpatterns = [
    path('', views.index),
    # path('new/', views.new),
    path('create/', views.create),
    path('<int:article_id>/', views.detail),
]