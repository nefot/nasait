from tkinter.constants import CASCADE

from django.db import models
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()


class Announcement(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='', null=True, blank=True, verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Анонс"
        verbose_name_plural = "Анонсы"

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='news_images/', blank=True, null=True, verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title


class Events(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='news_images/', blank=True, null=True, verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"

    def __str__(self):
        return self.title


# class Section(models.Model):
#     title = models.CharField(max_length=255, verbose_name="Название раздела")
#     published = models.BooleanField(default=False, verbose_name="Опубликовано?")
#
#     def __str__(self):
#         return self.title

class Files(models.Model):
    # Эти два поля нужны для GenericForeignKey
    subsection_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    subsection_id = models.PositiveIntegerField()
    subsection = GenericForeignKey('subsection_type', 'subsection_id')

    title = models.CharField(max_length=255, verbose_name="Название файла")
    content = models.FileField(verbose_name='Содержание', upload_to='uploads/')
    published = models.BooleanField(default=False, verbose_name="Опубликовано?")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"


class SubSection(models.Model):
    section = models.IntegerField()
    title = models.CharField(max_length=255, verbose_name="Название подраздела")
    content = CKEditor5Field(verbose_name='Содержание', config_name='extends')  # Поле для содержимого с CKEditor
    published = models.BooleanField(default=False, verbose_name="Опубликовано?")

    def __str__(self):
        return f"{self.title} - {self.title}"

    class Meta:
        verbose_name = "SubSection"
        verbose_name_plural = "SubSection"


class Organization(models.Model):
    section = models.IntegerField()
    title = models.CharField(max_length=255, verbose_name="Название подраздела")
    content = CKEditor5Field(verbose_name='Содержание', config_name='extends')  # Поле для содержимого с CKEditor
    published = models.BooleanField(default=False, verbose_name="Опубликовано?")

    def __str__(self):
        return f"{self.title} - {self.title}"

    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organization"


class Materials(models.Model):
    section = models.IntegerField()
    title = models.CharField(max_length=255, verbose_name="Название подраздела")
    content = CKEditor5Field(verbose_name='Содержание', config_name='extends')  # Поле для содержимого с CKEditor
    published = models.BooleanField(default=False, verbose_name="Опубликовано?")

    def __str__(self):
        return f"{self.title} - {self.title}"

    class Meta:
        verbose_name = "Materials"
        verbose_name_plural = "Materials"


class Base(models.Model):
    section = models.IntegerField()
    title = models.CharField(max_length=255, verbose_name="Название подраздела")
    content = CKEditor5Field(verbose_name='Содержание', config_name='extends')  # Поле для содержимого с CKEditor
    published = models.BooleanField(default=False, verbose_name="Опубликовано?")

    def __str__(self):
        return f"{self.title} - {self.title}"

    class Meta:
        verbose_name = "Специалистам"
        verbose_name_plural = "Специалистам"


class SiteSettings(models.Model):
    main_title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    block1_name = models.CharField(max_length=100)
    block2_name = models.CharField(max_length=100)
    block3_name = models.CharField(max_length=99)
    site_name = models.CharField(max_length=255, verbose_name="Название сайта")
    logo = models.ImageField(upload_to='settings/', blank=True, null=True, verbose_name="Логотип")
    contact_email = models.EmailField(blank=True, null=True, verbose_name="Контактный email")
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Номер телефона")
    address = models.TextField(blank=True, null=True, verbose_name="Адрес")
    facebook_link = models.URLField(blank=True, null=True, verbose_name="Facebook")
    twitter_link = models.URLField(blank=True, null=True, verbose_name="Twitter")
    instagram_link = models.URLField(blank=True, null=True, verbose_name="Instagram")

    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта"

    def __str__(self):
        return "Настройки сайта"
