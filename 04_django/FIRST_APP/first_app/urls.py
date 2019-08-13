
from django.contrib import admin
from django.urls import path, include
from pages import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('home/', views.home),
    path('lotto/', views.lotto),
    path('cube/<int:num>/', views.cube),
    path('match/', views.match),   
    path('artii/', include('artii.urls')),
]