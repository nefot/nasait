from django.contrib import admin
from .models import *

# Регистрация моделей в админке


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'location')


