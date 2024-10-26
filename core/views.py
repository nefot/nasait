from django.shortcuts import render

from core.models import Announcement, News, Events

from .models import SiteSettings


def index(request):
    announcements = Announcement.objects.all().order_by('-created_at')
    news_items = News.objects.all().order_by('-created_at')  # получаем все новости, сортированные по дате
    events = Events.objects.all().order_by('-created_at')  # получаем все новости, сортированные по дате
    site_settings = SiteSettings.objects.first()
    # print(site_settings.values())
    return render(request, 'index.html', {'announcements': announcements, 'news_items': news_items, 'events': events, 'site_settings': site_settings
})

# Create your views here.
