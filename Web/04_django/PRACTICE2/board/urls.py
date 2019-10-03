from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    # path('create/', views.create),
    path('<int:article_id>/', views.show, name='show'),
    path('<int:article_id>/delete/', views.delete, name='delete'),    
]