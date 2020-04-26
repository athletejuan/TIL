from django.urls import path
from . import views

app_name = 'eithers'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:question_id>/', views.detail, name='detail'),
]