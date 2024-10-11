from django.contrib import admin
from .models import *

# Регистрация моделей в админке

@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_catalog')


@admin.register(CategoryBook)
class CategoryBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_subdirectory', 'catalog')


@admin.register(Basket_item)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('id', 'count')


@admin.register(ProductCard)
class ProductCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock', 'rating', 'is_active')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'location')





@admin.register(LegalEntity)
class LegalEntityAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'TIN', 'legal_address')


@admin.register(PublishingHouse)
class PublishingHouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(BookSeries)
class BookSeriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_series')


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ISBN', 'price', 'year')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'books', 'rating', 'plus', 'minus')


@admin.register(DeliveryBook)
class DeliveryBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'method', 'price', 'day')


@admin.register(Imagess)
class ImagessAdmin(admin.ModelAdmin):
    list_display = ('id', 'img', 'data')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'patronymic')


@admin.register(Favorites)
class FavoritesAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_card')


@admin.register(Critique)
class CritiqueAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subtitle', 'product_card')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_news', 'date_news', 'is_published')


@admin.register(Help)
class HelpAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'count')


@admin.register(ContentBlock)
class ContentBlockAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'news')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_tag', 'color')
