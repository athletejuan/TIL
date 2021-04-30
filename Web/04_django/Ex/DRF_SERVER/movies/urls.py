from django.urls import path
from . import views

urlpatterns = [
    path('movie/', views.movie_list_create),
    path('movie/<int:movie_pk>/', views.movie_detail),
    path('review/', views.review_list),
    path('movie/<int:movie_pk>/review/', views.review_create),
    path('review/<int:review_pk>/', views.review_detail_update_delete),
    path('comment/', views.comment_list),
    path('review/<int:review_pk>/comment/', views.comment_create),
    path('comment/<int:comment_pk>/', views.comment_detail_update_delete),
]