
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls')),
    path('artii/', include('artii.urls')),    
    path('accounts/', include('accounts.urls')),
]