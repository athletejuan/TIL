from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/delete/', views.delete, name='delete'),
    path('<int:article_id>/update/', views.update, name='update'),
    path('<int:article_id>/comments/', views.comments_create, name='comments_create'),
    path('<int:article_id>/comments/<int:comment_id>/delete/', views.comments_delete, name='comments_delete'),
    path('<int:article_id>/like/', views.like, name='like'),
    path('<int:article_id>/follow/<int:user_id>/', views.follow, name='follow'),
]