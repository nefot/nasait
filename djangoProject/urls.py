from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static

from core.views import index
from djangoProject import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index)
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
