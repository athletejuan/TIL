from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),     # 반드시 path('accounts/', include('accounts.urls')), 아래에 와야한다.
    path('board/', include('board.urls')),
    path('admin/', admin.site.urls),    
]
