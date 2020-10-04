from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list_create),
    path('<int:article_pk>/', views.article_detail_update_delete),
]
