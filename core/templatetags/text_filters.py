# myapp/templatetags/text_filters.py
from django import template

register = template.Library()

@register.filter
def truncate_text(value, length=100):
    """Обрезает текст до заданной длины и добавляет 'Читать подробнее...'"""
    if len(value) > length:
        return f'{value[:length]}... <a href="#">Читать подробнее</a>'
    return value
