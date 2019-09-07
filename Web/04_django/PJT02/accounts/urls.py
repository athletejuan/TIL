from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login),
    path('logout/', views.logout),
    path('delete/', views.delete),
    path('edit/', views.edit),
    path('password/', views.change_password),
]
