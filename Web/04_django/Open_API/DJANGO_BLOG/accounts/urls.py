from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('quit/', views.quit, name='quit'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
]