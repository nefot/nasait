# news/admin.py
from celery.app.events import Events
from django.contrib import admin
from .models import Announcement, News,Events






from django.contrib import admin
from .models import SiteSettings

from django.contrib import admin
from django.db.utils import ProgrammingError

from core.models import SiteSettings

#
# class SiteSettingsAdmin(admin.ModelAdmin):
#     # Create a default object on the first page of SiteSettingsAdmin with a list of settings
#     def __init__(self, model, admin_site):
#         super().__init__(model, admin_site)
#         # be sure to wrap the loading and saving SiteSettings in a try catch,
#         # so that you can create database migrations
#         try:
#             SiteSettings.load().save()
#         except ProgrammingError:
#             pass
#
#     # prohibit adding new settings
#     def has_add_permission(self, request, obj=None):
#         return False
#
#     # as well as deleting existing
#     def has_delete_permission(self, request, obj=None):
#         return False
#
#
# admin.site.register(SiteSettings, SiteSettingsAdmin)
#

from .models import SiteSettings

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    # Запрет на добавление новой записи, если одна уже существует
    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    # Запрет на удаление существующей записи
    def has_delete_permission(self, request, obj=None):
        return False

    # Ограничение прав доступа только для суперпользователей
    def has_module_permission(self, request):
        return request.user.is_superuser

    # Настройки отображения полей в админке
    list_display = ('site_name', 'contact_email', 'phone_number',)
    fieldsets = (
        (None, {
            'fields': ('main_title', 'subtitle', 'block1_name', 'block2_name', 'block3_name')
        }),
        ('Основные настройки сайта', {
            'fields': ('site_name', 'logo', 'contact_email', 'phone_number', 'address')
        }),
        ('Социальные сети', {
            'fields': ('facebook_link', 'twitter_link', 'instagram_link')
        }),
    )





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