from django.contrib import admin
from django.urls import path

from home import views

urlpatterns = [
    path('home/palin/', views.palin),
    path('home/word/', views.word),
    path('home/ispal/<word>/', views.ispal),
    path('home/image/', views.image),
    path('home/template_language/', views.template_language),
    path('home/square/<int:weight>/<int:height>/', views.square),
    path('home/hello/<name>/', views.hello),
    path('home/lotto/', views.lotto),
    path('home/dinner/', views.dinner),
    path('home/hola/', views.hola),
    path('home/index/', views.index),
    path('admin/', admin.site.urls),
]
