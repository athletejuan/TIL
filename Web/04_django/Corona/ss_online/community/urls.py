from django.urls import path
from . import views

app_name = "community"

urlpatterns = [
    path('', views.review_list, name="review_list"),
    path('new_review/', views.new_review, name="new_review"),
    # path('review_create/', views.review_create, name="review_create"),
    path('<int:review_id>/', views.review_detail, name="review_detail"),
]