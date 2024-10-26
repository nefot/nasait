# news/admin.py
from celery.app.events import Events
from django.contrib import admin
from .models import Announcement, News,Events

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title',)
    ordering = ('-created_at',)

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'image')
        }),
        # Убираем 'created_at' из fieldsets, чтобы избежать ошибки
    )
    readonly_fields = ('created_at',)  # Поле будет только для чтения (отображение), но не для редактирования

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title',)
    ordering = ('-created_at',)

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'image')
        }),
    )

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title',)
    ordering = ('-created_at',)

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'image')
        }),
    )