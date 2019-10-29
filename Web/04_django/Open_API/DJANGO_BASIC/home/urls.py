from django.urls import path
from . import views

urlpatterns = [
    path('static_example/', views.static_example),
    path('user_create/', views.user_create),
    path('user_new/', views.user_new),
    path('palin/', views.palin),
    path('word/', views.word),
    path('catch/', views.catch),
    path('throw/', views.throw),
    path('ispal/<word>/', views.ispal),
    path('isbirth/', views.isbirth),
    path('image/', views.image),
    path('template_language/', views.template_language),
    path('square/<int:weight>/<int:height>/', views.square),
    path('introduce/<name>/<int:age>/', views.introduce),
    path('hello/<name>/', views.hello),
    path('lotto/', views.lotto),
    path('dinner/', views.dinner),
    path('hola/', views.hola),
    path('index/', views.index),
]