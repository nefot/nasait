from django.db import models

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

