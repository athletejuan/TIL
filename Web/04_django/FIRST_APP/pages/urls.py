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
    path('static_example/', views.static_example, name='static_example'),
    path('bootstrap_example/', views.bootstrap_example, name='bootstrap_example'),
    path('exchange/', views.exchange, name='exchange'),
]