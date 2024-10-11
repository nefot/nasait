from django.db import models
# from backet.models import Basket
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=50, blank=False)
    password = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=50, unique=True, blank=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, unique=True, blank=False)
    address = models.CharField(max_length=50)
    index = models.CharField(max_length=50)

    # basket = models.ForeignKey(Basket, on_delete=models.CASCADE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'patronymic', 'phone']

    def __str__(self):
        return self.username

#
# class User():
#     username = models.CharField(max_length=50, blank=False)
#     password = models.CharField(max_length=50, blank=False)
#     email = models.EmailField(max_length=50, unique=True, blank=False)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     patronymic = models.CharField(max_length=50)
#     phone = models.CharField(max_length=50, unique=True, blank=False)
#     address = models.CharField(max_length=50)
#     index = models.CharField(max_length=50)
#
#     basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
#
#
#     def __str__(self):
#         return self.username
