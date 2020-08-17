from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('dinner/<str:menu>/<int:peoples>/', views.dinner),
    path('lotto/', views.lotto),
    path('admin/', admin.site.urls),
]
