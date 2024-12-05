p# # yourapp/context_processors.py
#  # Обработка случая, если нет настроек
# from core.models import SiteSettings
#
#
# def load_settings(request):
#     try:
#         return {'site_settings': SiteSettings.load()}
#     except SiteSettings.DoesNotExist:
#         return {'site_settings': None}