from django.urls import path
from . import views

urlpatterns = [
    path('html/', views.article_list_html),
    path('json_1/', views.article_list_json_1),
    path('json_2/', views.article_list_json_2),
    path('json_3/', views.article_list_json_3),
]