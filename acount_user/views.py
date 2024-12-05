from django.shortcuts import render
from django.shortcuts import render
from core.models import SiteSettings
from core.models import *
from django.template import loader
import re
from django.utils.html import format_html

from django.views.generic import DetailView
from core.models import Page


class SubsectionDetailView(DetailView):
    model = Page
    template_name = "subsection_detail.html"


def replace_file_tags(text):
    # Регулярное выражение для поиска `[file:<id>]`
    pattern = r'\[file:(\d+)\]'

    def replace_match(match):
        file_id = match.group(1)  # Получаем ID из совпадения
        try:
            document = Files.objects.get(id=file_id)  # Находим файл по ID
            # Возвращаем HTML-ссылку на файл
            return format_html('<a href="{}" download>{}</a>', document.file.url, document.title)
        except Files.DoesNotExist:
            return '[Файл не найден]'

    # Заменяем все совпадения в тексте
    return re.sub(pattern, replace_match, text)


def home(request):
    return render(request, 'index.html')  # Главная страница


def specialists(request):
    subsections = SubSection.objects.filter(published=True).order_by('section')

    # Привязка файлов к каждому подразделу
    for subsection in subsections:
        subsection.files = Files.objects.filter(
            subsection_type=ContentType.objects.get_for_model(SubSection),
            subsection_id=subsection.id,
            published=True
        )

    return render(request, 'specialists.html', {
        'subsections': subsections,
        'site_settings': SiteSettings.objects.first()
    })


def organisation(request):
    subsections = Organization.objects.filter(published=True).order_by('section')

    # Привязка файлов к каждому подразделу
    for subsection in subsections:
        subsection.files = Files.objects.filter(
            subsection_type=ContentType.objects.get_for_model(Organization),
            subsection_id=subsection.id,
            published=True
        )

    return render(request, 'organizations.html', {
        'subsections': subsections,
        'site_settings': SiteSettings.objects.first()
    })


def organization_medical_prevention(request):
    subsections = Organization.objects.filter(published=True).order_by('section')

    # Привязка файлов к каждому подразделу
    for subsection in subsections:
        subsection.files = Files.objects.filter(
            subsection_type=ContentType.objects.get_for_model(Organization),
            subsection_id=subsection.id,
            published=True
        )

    return render(request, 'orgia.html', {
        'subsections': subsections,
        'site_settings': SiteSettings.objects.first()
    })


def legal_framework(request):
    subsections = Base.objects.filter(published=True).order_by('section')

    # Привязка файлов к каждому подразделу
    for subsection in subsections:
        subsection.files = Files.objects.filter(
            subsection_type=ContentType.objects.get_for_model(Base),
            subsection_id=subsection.id,
            published=True
        )

    return render(request, 'legal_framework.html', {
        'subsections': subsections,
        'site_settings': SiteSettings.objects.first()
    })


def reference_materials(request):
    subsections = Materials.objects.filter(published=True).order_by('section')

    # Привязка файлов к каждому подразделу
    for subsection in subsections:
        subsection.files = Files.objects.filter(
            subsection_type=ContentType.objects.get_for_model(Materials),
            subsection_id=subsection.id,
            published=True
        )

    return render(request, 'reference_materials.html', {
        'subsections': subsections,
        'site_settings': SiteSettings.objects.first()
    })


def news_detail(request):
    return render(request, 'news_page.html')
