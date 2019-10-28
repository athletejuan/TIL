from django.contrib import admin
from django.urls import path

from home import views

urlpatterns = [
    path('home/static_example/', views.static_example),
    path('home/user_create/', views.user_create),
    path('home/user_new/', views.user_new),
    path('home/palin/', views.palin),
    path('home/word/', views.word),
    path('home/catch/', views.catch),
    path('home/throw/', views.throw),
    path('home/ispal/<word>/', views.ispal),
    path('home/isbirth/', views.isbirth),
    path('home/image/', views.image),
    path('home/template_language/', views.template_language),
    path('home/square/<int:weight>/<int:height>/', views.square),
    path('home/introduce/<name>/<int:age>/', views.introduce),
    path('home/hello/<name>/', views.hello),
    path('home/lotto/', views.lotto),
    path('home/dinner/', views.dinner),
    path('home/hola/', views.hola),
    path('home/index/', views.index),
    path('admin/', admin.site.urls),
]
