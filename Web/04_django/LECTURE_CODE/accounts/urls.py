from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('<username>/profile/', views.profile, name='profile'),
    path('<int:user_pk>/password/', views.change_password, name='change_password'),
    path('<int:user_pk>/edit/', views.edit, name='edit'),
    path('<int:user_pk>/delete/', views.delete, name='delete'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('', views.index, name='index'),
]