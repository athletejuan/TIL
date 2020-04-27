from django.urls import path
from . import views

app_name = 'eithers'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('random/', views.random_issue, name='random_issue'),
    path('<int:question_pk>/', views.detail, name='detail'),
    path('<int:question_pk>/comments/', views.comment_create, name='comment_create'),
]