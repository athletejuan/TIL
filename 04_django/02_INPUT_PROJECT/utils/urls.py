from django.urls import path
from . import views

# 'utils/'
urlpatterns = [
    path('', views.index), # utils/
    path('art/', views.art), # utils/art/
    path('output/', views.output), # utils/output/
    path('throw/', views.throw),
    path('catch/', views.catch),
]