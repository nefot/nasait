from django.shortcuts import render
from django.shortcuts import render
def home(request):
    return render(request, 'index.html')  # Главная страница

def specialists(request):
    return render(request, 'specialists.html')  # Страница "Специалисты"

def organizations(request):
    return render(request, 'organizations.html')  # Страница "Организации"

def reference_materials(request):
    return render(request, 'reference_materials.html')  # Страница "Справочные материалы"

def legal_framework(request):
    return render(request, 'legal_framework.html')  # Страница "Нормативно-правовая база"
# news/views.py

