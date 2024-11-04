from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from core import views
from core.views import index

from djangoProject import settings

urlpatterns = [

    # для AJAX

    # path('myapp/', include('core.urls')),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('admin/', admin.site.urls),         # Админка
    path('', index, name='home'),            # Главная страница
    path('account/', include('acount_user.urls')),  # URL-ы из приложения account_user
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)

