from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    # path('create/', views.create),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/edit/', views.edit),
    path('<int:article_id>/delete/', views.delete),
    path('<int:article_id>/create_comment/', views.create_comment)
]