from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('movies/', include('movies.urls')),
    path('jobs/', include('jobs.urls')),
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 첫번째 인자: 어떤 URL을 정적으로 추가 할지 (Media file URL)
# 두번째 인자: 실제 해당 미디어 파일은 어디에 있는지 / 이때 document_root는 키워드인자로 Media File 이 위치한 경로로 전달.