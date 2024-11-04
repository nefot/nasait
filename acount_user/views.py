from django.shortcuts import render
from django.shortcuts import render

from core.models import *


def home(request):
    return render(request, 'index.html')  # Главная страница


def specialists(request):
    subsections = SubSection.objects.filter(published=True).order_by('section')
    return render(request, 'specialists.html', {'subsections': subsections})

def organisation(request):
    subsections = Organization.objects.filter(published=True).order_by('section')
    return render(request, 'organizations.html', {'subsections': subsections})
def legal_framework(request):
    subsections = Base.objects.filter(published=True).order_by('section')
    return render(request, 'legal_framework.html', {'subsections': subsections})
def reference_materials(request):
    subsections = Materials.objects.filter(published=True).order_by('section')
    return render(request, 'reference_materials.html', {'subsections': subsections})
# news/views.py

