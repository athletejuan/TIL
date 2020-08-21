from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('community/', include('community.urls')),
    path('admin/', admin.site.urls),
]
