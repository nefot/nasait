from django.urls import path
from . import views  # Импортируем views из вашего приложения

urlpatterns = [
    # path('', views.home, name='home'),  # Главная страница
    path('news-detail/', views.news_detail, name='news_detail'),
    path('specialists/', views.specialists, name='specialists'),
    path('organizations/', views.organisation, name='organizations'),
    path('reference-materials/', views.reference_materials, name='reference_materials'),
    path('legal-framework/', views.legal_framework, name='legal_framework'),
    path('organization_medical_prevention/', views.specialists, name='orgia'),
]
