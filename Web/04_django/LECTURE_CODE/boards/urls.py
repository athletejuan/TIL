from django.urls import path
from boards import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    # path('new/', views.new),
    path('create/', views.create, name='create'),
    path('<int:article_id>/', views.detail, name='detail'),
    # path('<int:article_id>/edit/', views.edit),
    path('<int:article_id>/update/', views.update, name='update'),
    path('<int:article_id>/delete/', views.delete, name='delete'),
    path('<int:article_id>/comment/', views.create_comment, name='comment'),
    path('<int:article_id>/comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]