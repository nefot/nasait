from django.db import models
# from backet.models import Basket
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    name = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    email =models.EmailField(max_length=50, unique=True, blank=False,)
    img = models.CharField(max_length=255, null=True, blank=True)
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

# news/models.py
from django.db import models

