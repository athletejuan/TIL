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
    path('kospi/', views.kospi, name='kospi'),
    path('template_language/', views.template_language, name='template_language'),
    path('image/', views.image, name='image'),
    path('ispal/<word>/', views.ispal, name='ispal'),
    path('word/', views.word, name='word'),
    path('palin/', views.palin, name='palin'),
]