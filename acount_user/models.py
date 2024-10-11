from django.db import models
# from backet.models import Basket
from django.contrib.auth.models import AbstractUser


class Basket_item(models.Model):
    product = models.ForeignKey('Books', on_delete=models.CASCADE)
    count = models.IntegerField(null=True, blank=True)


class Basket(models.Model):
    basket_item = models.ForeignKey('Basket_item', on_delete=models.CASCADE)


class User(AbstractUser):
    basket = models.OneToOneField(Basket, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    favorites = models.ForeignKey('Favorites', on_delete=models.SET_NULL, null=True, blank=True)
    email =models.EmailField(max_length=50, unique=True, blank=False,)
    legal_entity = models.OneToOneField('LegalEntity', related_name='users' ,on_delete=models.SET_NULL, null=True)
    img = models.CharField(max_length=255, null=True, blank=True)
    imagess = models.OneToOneField('Imagess', on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    partonymic = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    adress = models.CharField(max_length=255, null=True, blank=True)
    index = models.CharField(max_length=255, null=True, blank=True)
    # reviews = models.ManyToManyField('Review', related_name='reviewed_by_users')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]


def __str__(self):
    return self.username


class Catalog(models.Model):
    name_catalog = models.CharField(max_length=255, null=True, blank=True)


class CategoryBook(models.Model):
    name_subdirectory = models.CharField(max_length=255, null=True, blank=True)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name='subdirectories')


class ProductCard(models.Model):
    stock = models.BooleanField(default=False)
    article_number = models.CharField(max_length=255, null=True, blank=True)
    weight = models.CharField(max_length=255, null=True, blank=True)
    size_x = models.CharField(max_length=255, null=True, blank=True)
    size_y = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    info_reviews = models.TextField(null=True, blank=True)
    info_delivery = models.TextField(null=True, blank=True)
    info_purchase = models.TextField(null=True, blank=True)
    info_buy = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True)
    rating = models.CharField(max_length=255, null=True, blank=True)
    discount = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    ISBN = models.CharField(max_length=13, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    basket = models.ManyToManyField(Basket_item, related_name='product_cards', blank=True)


class LegalEntity(models.Model):
    company_name = models.CharField(max_length=255, null=True, blank=True)
    legal_address = models.CharField(max_length=255, null=True, blank=True)
    TIN = models.CharField(max_length=12, null=True, blank=True)
    KPP = models.CharField(max_length=9, null=True, blank=True)
    bank_account = models.CharField(max_length=20, null=True, blank=True)
    BIK = models.CharField(max_length=9, null=True, blank=True)
    correspondent_account = models.CharField(max_length=20, null=True, blank=True)
    commentary = models.TextField(null=True, blank=True)


class PublishingHouse(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)


class BookSeries(models.Model):
    name_series = models.CharField(max_length=255, null=True, blank=True)


class Books(ProductCard):
    authors = models.ManyToManyField('Author', related_name='books', blank=True)
    year = models.IntegerField(null=True, blank=True)
    publishing_houses = models.ManyToManyField(PublishingHouse, related_name='books', blank=True)
    categories = models.ManyToManyField(CategoryBook, related_name='books', blank=True)
    book_series = models.ManyToManyField(BookSeries, related_name='books', blank=True)
    file = models.CharField(max_length=255, null=True, blank=True)
    audio = models.CharField(max_length=255, null=True, blank=True)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    books = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(null=True, blank=True)
    plus = models.TextField(null=True, blank=True)
    minus = models.TextField(null=True, blank=True)
    date = models.CharField(max_length=255, null=True, blank=True)


class DeliveryBook(models.Model):
    method = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    day = models.CharField(max_length=255, null=True, blank=True)


class Imagess(models.Model):
    img = models.CharField(max_length=255, null=True, blank=True)
    data = models.TextField(null=True, blank=True)
    product_card = models.ForeignKey(ProductCard, on_delete=models.SET_NULL, null=True, blank=True)


class Author(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    patronymic = models.CharField(max_length=255, null=True, blank=True)
    images = models.ManyToManyField(Imagess, related_name='author_images', blank=True)


class Favorites(models.Model):
    product_card = models.ForeignKey(ProductCard, on_delete=models.CASCADE)


class Critique(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    product_card = models.ForeignKey(ProductCard, on_delete=models.CASCADE, related_name='critiques')


class News(models.Model):
    name_news = models.CharField(max_length=255, null=True, blank=True)
    date_news = models.CharField(max_length=255, null=True, blank=True)
    images = models.ManyToManyField(Imagess, related_name='news_images', blank=True)
    is_published = models.BooleanField(default=False)


class Help(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(null=True, blank=True)


class Orders(Basket_item):
    pass


class ContentBlock(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    img = models.CharField(max_length=255, null=True, blank=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='content_blocks')


class Tag(models.Model):
    name_tag = models.CharField(max_length=255, null=True, blank=True)
    color = models.IntegerField(null=True, blank=True)
    product_cards = models.ManyToManyField(ProductCard, related_name='tags', blank=True)
