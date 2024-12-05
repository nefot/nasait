from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from core.views import index
from djangoProject import settings

urlpatterns = [
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('account/', include('acount_user.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
