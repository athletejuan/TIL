from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
    path('community/', include('community.urls')),
    path('eithers/', include('eithers.urls')),
    path('', views.index),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
