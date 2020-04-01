from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list),
    path('new_review/', views.new_review),
    path('review_create/', views.review_create),
    path('<int:review_id>/', views.review_detail),
]