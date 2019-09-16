from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.create, name='create'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/update/', views.update, name='update'),
    path('<int:article_id>/delete/', views.delete, name='delete'),
    path('<int:article_id>/create_comment/', views.create_comment)
]