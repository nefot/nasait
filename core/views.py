from django.shortcuts import render

from core.models import Announcement, News, Events


def index(request):
    announcements = Announcement.objects.all().order_by('-created_at')
    news_items = News.objects.all().order_by('-created_at')  # получаем все новости, сортированные по дате
    events = Events.objects.all().order_by('-created_at')  # получаем все новости, сортированные по дате

    return render(request, 'index.html', {'announcements': announcements, 'news_items': news_items, 'events': events})

# Create your views here.
