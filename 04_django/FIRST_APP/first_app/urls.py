
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('home/', views.home),
    path('lotto/', views.lotto),
    path('cube/<int:num>/', views.cube),
    path('match/', views.match),
]