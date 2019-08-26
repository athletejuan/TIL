from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/delete/', views.delete, name='delete'),
    path('<int:article_id>/edit/', views.edit, name='edit'),
]