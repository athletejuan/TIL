from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('movies/', include('movies.urls')),
    path('jobs/', include('jobs.urls')),
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
]
