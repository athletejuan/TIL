from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.review_list, name='review_list'),
    path('create/', views.create, name='create'),
    path('<int:review_pk>/', views.detail, name='detail'),
    path('<int:review_pk>/update/', views.update, name='update'),
    path('<int:review_pk>/delete/', views.delete, name='delete'),
]
