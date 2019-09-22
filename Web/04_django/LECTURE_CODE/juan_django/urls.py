from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('boards/', include('boards.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 다른 방식
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# /media/ 들어오는 요청들을 통과시켜주세요.
# static()