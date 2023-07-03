from django.db import models
from django.contrib.auth.models import AbstractUser


class Organization(models.Model):
    name = models.CharField(max_length=255, unique=True, default='default')

    def __str__(self):
        return self.name


class User(AbstractUser):
    default = 'Пользователь'
    ord_admin = 'Администратор организации'
    admin = 'Главный администратор'

    CATEGORY_TYPES = [
        (default, 'Пользователь'),
        (ord_admin, 'Администратор организации'),
        (admin, 'Главный администратор'),
    ]

    name = models.CharField(max_length=255)
    post = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    communications = models.CharField(max_length=255)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)
    role = models.CharField(max_length=255, choices=CATEGORY_TYPES, default=default)

