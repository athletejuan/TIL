from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.review_list, name='review_list'),
    path('new/', views.new_review, name='new_review'),
    path('<int:pk>/', views.review_detail, name='review_detail'),
]