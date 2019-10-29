from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('home/', include('home.urls')),
    path('utilities/', include('utilities.urls')),
    path('admin/', admin.site.urls),
]
