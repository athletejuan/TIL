from django.urls import path
from . import views

urlpatterns = [
    # Create
    path('articles/new/', views.new), # /board/articles/new/
    path('articles/create/', views.create), # /board/articles/create/
    # Read
    path('articles/', views.index), # /board/articles
    path('articles/<int:article_id>/', views.show), # /board/articles/show/
    # Update
    # Delelte
    path('articles/<int:article_id>/delete/', views.delete), # /board/articles/1/delete/
]   