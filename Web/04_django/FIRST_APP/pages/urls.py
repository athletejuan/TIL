from django.urls import path
from . import views

app_name= 'pages'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('lotto/', views.lotto, name='lotto'),
    path('cube/<int:num>/', views.cube, name='cube'),
    path('match/', views.match, name='match'),
    path('dtl/', views.dtl, name='dtl'),
]