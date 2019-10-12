from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('boards/', include('boards.urls')),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
