from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    # path('create/', views.create, name='create'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/edit/', views.edit, name='edit'),
    path('<int:article_id>/delete/', views.delete, name='delete'),
    path('<int:article_id>/comments/create/', views.comments_create, name='comments_create'),
    path('<int:article_id>/comments/<int:comment_id>/delete/', views.comments_delete, name='comments_delete'),
]