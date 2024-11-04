# news/admin.py
from celery.app.events import Events
from django.contrib import admin
from .models import *
from django.contrib import admin


class SubSectionInline(admin.StackedInline):  # или TabularInline для компактного отображения
    model = SubSection
    extra = 1  # Количество пустых полей для новых подразделов
    fields = ['title', 'content', 'published']
    verbose_name = "Подраздел"
    verbose_name_plural = "Подразделы"

# @admin.register(Section)
# class SectionAdmin(admin.ModelAdmin):
#     list_display = ['title', 'published']
#     inlines = [SubSectionInline]  # Встраиваем SubSection в Section
#
#     fieldsets = (
#         (None, {
#             'fields': ('title', 'published'),
#         }),
#     )

@admin.register(SubSection)
class SubSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'section', 'published']
    list_filter = ['section', 'published']


@admin.register(Organization)
class SubSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'section', 'published']
    list_filter = ['section', 'published']

@admin.register(Materials)
class SubSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'section', 'published']
    list_filter = ['section', 'published']

@admin.register(Base)
class SubSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'section', 'published']
    list_filter = ['section', 'published']

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