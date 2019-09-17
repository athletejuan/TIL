from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('board/', include('board.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 다른 방식
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# /media/ 들어오는 요청들을 통과 시켜주세요.
# static()
