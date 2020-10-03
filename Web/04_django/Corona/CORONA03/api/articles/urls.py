from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list_create),
    # path('create/', views.create_article),
    path('<int:article_pk>/', views.article_detail_update_delete),
    # path('<int:article_pk>/delete/', views.delete_article),
    # path('<int:article_pk>/update/', views.update_article),
    path('<int:article_pk>/comments/', views.create_comment),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail_update_delete),
    path('html/', views.article_list_html),
    path('json_1/', views.article_list_json_1),
    path('json_2/', views.article_list_json_2),
    path('json_3/', views.article_list_json_3),
]