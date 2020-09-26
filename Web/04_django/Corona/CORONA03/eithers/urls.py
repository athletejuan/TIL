from django.urls import path
from . import views

app_name = 'eithers'

urlpatterns = [
    path('', views.main, name='main'),
    path('create/', views.create, name='create'),
    path('random/', views.random_question, name='random'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/comments/', views.comments, name='comments'),
    path('<int:pk>/delete/', views.delete, name="delete"),
]
