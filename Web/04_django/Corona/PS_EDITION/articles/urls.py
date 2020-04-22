from django.urls import path
from articles import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    # path('new/', views.new),
    path('create/', views.create, name='create'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/like/', views.like, name='like'),
]