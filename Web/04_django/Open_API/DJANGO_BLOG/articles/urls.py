from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('<int:id>/delete/', views.delete, name='delete'),    # articles/1/delete/, articles/2/delete/ ...
    path('<int:id>/update/', views.update, name='update'),     # articles/3/update/, articles/4/update/ ...
    # path('<int:id>/edit/', views.edit, name='edit'),     # articles/2/edit/, articles/4/edit/ ...
    path('<int:id>/', views.detail, name='detail'),    # articles/1/, articles/2/ ...
    path('create/', views.create, name='create'),    # articles/create/
    # path('new/', views.new, name='new'),    # articles/new/
    path('', views.index, name='index'),    # articles/
]