from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]