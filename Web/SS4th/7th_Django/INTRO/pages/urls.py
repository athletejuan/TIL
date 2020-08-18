from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('community/', views.community, name="community"),
    path('card/', views.card, name="card"),
    path('dinner/<str:menu>/<int:peoples>/', views.dinner, name="dinner"),
    path('lotto/', views.lotto, name="lotto"),
]