# news/admin.py
from email._header_value_parser import Section

from celery.app.events import Events
from django.contrib import admin
from .models import *
from django.contrib import admin

from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline


class FilesInline(GenericTabularInline):
    model = Files
    ct_field = "subsection_type"  # Поле для типа контента
    ct_fk_field = "subsection_id" # Поле для ID связанного объекта
    extra = 1


@admin.register(SubSection)
class SectionAdmin(admin.ModelAdmin):
    inlines = [FilesInline]

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    inlines = [FilesInline]

@admin.register(Materials)
class MaterialsAdmin(admin.ModelAdmin):
    inlines = [FilesInline]

@admin.register(Base)
class BaseAdmin(admin.ModelAdmin):
    inlines = [FilesInline]

# Регистрируем саму модель Files без inline
# @admin.register(Files)
# class FilesAdmin(admin.ModelAdmin):
#     list_display = ('id','title', 'published')
#     list_filter = ('published',)
#     search_fields = ('title',)

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

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    # Отображаем поля в списке записей
    list_display = ('site_name', 'main_title', 'contact_email', 'phone_number')
    search_fields = ('site_name', 'contact_email')

    # Настраиваем группировку полей в админке
    fieldsets = (
        ("Основные настройки", {
            'fields': ('site_name', 'main_title', 'subtitle', 'logo')
        }),
        ("Блоки контента", {
            'fields': ('block1_name', 'block2_name', 'block3_name')
        }),
        ("Контактная информация", {
            'fields': ('contact_email', 'phone_number', 'address')
        }),
        ("Социальные сети", {
            'fields': ('facebook_link', 'twitter_link', 'instagram_link')
        }),
    )

    # Отключаем возможность добавления нескольких экземпляров SiteSettings
    def has_add_permission(self, request):
        # Разрешаем добавлять запись, если еще нет ни одной
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Отключаем возможность удаления
        return False

