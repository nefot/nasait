from django.shortcuts import render
from django.http import JsonResponse

from core.models import Announcement, News, Events, SubSection
from django.shortcuts import render, get_object_or_404
from .models import SiteSettings


def index(request):
    announcements = Announcement.objects.all().order_by('-created_at')
    news_items = News.objects.all().order_by('-created_at')
    events = Events.objects.all().order_by('-created_at')
    site_settings = SiteSettings.objects.first()
    return render(request, 'index.html', {
        'announcements': announcements,
        'news_items': news_items,
        'events': events,
        'site_settings': site_settings
        })
