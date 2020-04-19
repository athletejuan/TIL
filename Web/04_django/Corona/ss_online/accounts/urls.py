from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('delete/', views.delete, name='delete'),
    path('<int:pk>/', views.profile, name='profile'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/password/', views.change_password, name='change_password'),
]