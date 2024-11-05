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
    title = models.CharField(max_length=255, verbose_name="Заголовок", help_text="Основной заголовок анонса. Будет отображаться на сайте.")
    description = models.TextField(verbose_name="Описание", help_text="Полное описание анонса, содержащее все основные сведения.")
    image = models.ImageField(upload_to='announcements/', null=True, blank=True, verbose_name="Изображение", help_text="Загрузите изображение, которое будет представлять анонс.")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", help_text="Дата и время, когда анонс был создан.")

    class Meta:
        verbose_name = "Анонс"
        verbose_name_plural = "Анонсы"

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок", help_text="Основной заголовок новости, который будет отображаться на сайте.")
    description = models.TextField(verbose_name="Описание", help_text="Полный текст новости, включающий все важные детали.")
    image = models.ImageField(upload_to='news_images/', blank=True, null=True, verbose_name="Изображение", help_text="Загрузите изображение, представляющее новость.")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации", help_text="Дата и время публикации новости.")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title


class Events(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок", help_text="Основной заголовок события, который будет отображаться на сайте.")
    description = models.TextField(verbose_name="Описание", help_text="Полное описание события с деталями и важной информацией.")
    image = models.ImageField(upload_to='event_images/', blank=True, null=True, verbose_name="Изображение", help_text="Загрузите изображение, представляющее событие.")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации", help_text="Дата и время публикации события.")

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"

    def __str__(self):
        return self.title


class Files(models.Model):
    subsection_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name="Тип подраздела", help_text="Тип контента, к которому относится файл.")
    subsection_id = models.PositiveIntegerField(verbose_name="ID подраздела", help_text="ID объекта контента, к которому относится файл.")
    subsection = GenericForeignKey('subsection_type', 'subsection_id')
    title = models.CharField(max_length=255, verbose_name="Название файла", help_text="Название файла, отображаемое на сайте.")
    content = models.FileField(upload_to='uploads/', verbose_name="Содержание", help_text="Файл для загрузки, доступный для пользователей сайта.")
    published = models.BooleanField(default=False, verbose_name="Опубликовано?", help_text="Отметьте, если файл готов к публикации и должен быть доступен на сайте.")

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"

    def __str__(self):
        return self.title


class SubSection(models.Model):
    section = models.IntegerField(verbose_name="Раздел", help_text="Номер раздела, к которому относится этот подраздел.")
    title = models.CharField(max_length=255, verbose_name="Название подраздела", help_text="Название подраздела, которое будет отображаться на сайте.")
    content = CKEditor5Field(verbose_name="Содержание", config_name='extends', help_text="Полный текст подраздела, отформатированный с помощью редактора.")
    published = models.BooleanField(default=False, verbose_name="Опубликовано?", help_text="Отметьте, если подраздел должен быть доступен на сайте.")

    class Meta:
        verbose_name = "Специалисты"
        verbose_name_plural = "Специалисты"

    def __str__(self):
        return self.title


class Organization(models.Model):
    section = models.IntegerField(verbose_name="Раздел", help_text="Номер раздела, к которому относится организация.")
    title = models.CharField(max_length=255, verbose_name="Название подраздела", help_text="Название подраздела с информацией об организации.")
    content = CKEditor5Field(verbose_name="Содержание", config_name='extends', help_text="Полный текст подраздела, отформатированный с помощью редактора.")
    published = models.BooleanField(default=False, verbose_name="Опубликовано?", help_text="Отметьте, если информация должна быть доступна на сайте.")

    class Meta:
        verbose_name = "Организации"
        verbose_name_plural = "Организации"

    def __str__(self):
        return self.title


class Materials(models.Model):
    section = models.IntegerField(verbose_name="Раздел", help_text="Номер раздела, связанного с материалами для аккредитации.")
    title = models.CharField(max_length=255, verbose_name="Название подраздела", help_text="Название подраздела с материалами для аккредитации.")
    content = CKEditor5Field(verbose_name="Содержание", config_name='extends', help_text="Полный текст подраздела, отформатированный с помощью редактора.")
    published = models.BooleanField(default=False, verbose_name="Опубликовано?", help_text="Отметьте, если подраздел должен быть доступен на сайте.")

    class Meta:
        verbose_name = "Для аккредитации"
        verbose_name_plural = "Для аккредитации"

    def __str__(self):
        return self.title


class Base(models.Model):
    section = models.IntegerField(verbose_name="Раздел", help_text="Номер раздела, связанного с базой информации для специалистов.")
    title = models.CharField(max_length=255, verbose_name="Название подраздела", help_text="Название подраздела с информацией для специалистов.")
    content = CKEditor5Field(verbose_name="Содержание", config_name='extends', help_text="Полный текст подраздела, отформатированный с помощью редактора.")
    published = models.BooleanField(default=False, verbose_name="Опубликовано?", help_text="Отметьте, если информация должна быть доступна на сайте.")

    class Meta:
        verbose_name = "База"
        verbose_name_plural = "База"

    def __str__(self):
        return self.title


class SiteSettings(models.Model):
    main_title = models.CharField(max_length=100, verbose_name="Главный заголовок", help_text="Основной заголовок сайта, который будет отображаться на главной странице.")
    subtitle = models.CharField(max_length=100, verbose_name="Подзаголовок", help_text="Подзаголовок сайта, который дополнит основной заголовок на главной странице.")
    block1_name = models.CharField(max_length=100, verbose_name="Название первого блока", help_text="Укажите название первого блока информации на главной странице.")
    block2_name = models.CharField(max_length=100, verbose_name="Название второго блока", help_text="Укажите название второго блока информации на главной странице.")
    block3_name = models.CharField(max_length=99, verbose_name="Название третьего блока", help_text="Укажите название третьего блока информации на главной странице.")
    site_name = models.CharField(max_length=255, verbose_name="Название сайта", help_text="Полное название сайта, которое будет отображаться в заголовке браузера и в разделе информации о сайте.")
    logo = models.ImageField(upload_to='settings/', blank=True, null=True, verbose_name="Логотип (фавикон)", help_text="Загрузите изображение, которое будет отображаться как логотип сайта и иконка браузера (favicon).")
    contact_email = models.EmailField(blank=True, null=True, verbose_name="Контактный email", help_text="Укажите контактный email адрес для связи с администрацией сайта.")
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Номер телефона", help_text="Основной контактный номер телефона для связи с администрацией.")
    address = models.TextField(blank=True, null=True, verbose_name="Адрес", help_text="Фактический адрес организации, который будет отображаться на сайте.")
    facebook_link = models.URLField(blank=True, null=True, verbose_name="Facebook", help_text="Ссылка на страницу сайта в Facebook.")
    twitter_link = models.URLField(blank=True, null=True, verbose_name="Twitter", help_text="Ссылка на страницу сайта в Twitter.")
    instagram_link = models.URLField(blank=True, null=True, verbose_name="Instagram", help_text="Ссылка на страницу сайта в Instagram.")

    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта"

    def __str__(self):
        return "Настройки сайта"
