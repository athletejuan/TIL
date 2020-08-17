from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('lotto/', views.lotto),
    path('admin/', admin.site.urls),
]
