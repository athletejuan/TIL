from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),
    path('delete/', views.delete, name='delete'),
    path('<username>/', views.profile, name='profile'),
    path('follow/<int:user_pk>/', views.follow, name='follow'),
    # path('<username>/follow/', views.follow, name='follow'),
]
