from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path('', views.index, name="index"),
    # path('new/', views.new),
    path('create/', views.create, name="create"),
    path('<int:article_id>/', views.detail, name="detail"),
    path('<int:article_id>/edit/', views.edit, name="update"),
    # path('<int:article_id>/update/', views.update),
    path('<int:article_id>/delete/', views.delete, name="delete"),
]