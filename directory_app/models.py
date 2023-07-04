from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class Organization(models.Model):
    name = models.CharField(max_length=255, unique=True, default='default')

    def __str__(self):
        return self.name


class CustomUserManager(BaseUserManager):
    def _create_user(self, name, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        if not name:
            raise ValueError('The Name field must be set')
        name = self.normalize_email(name)
        user = self.model(name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(name, password, **extra_fields)

    def create_superuser(self, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(name, password, **extra_fields)


class User(AbstractUser):
    first_name = None
    last_name = None

    default = 'Пользователь'
    ord_admin = 'Администратор организации'
    admin = 'Главный администратор'

    CATEGORY_TYPES = [
        (default, 'Пользователь'),
        (ord_admin, 'Администратор организации'),
        (admin, 'Главный администратор'),
    ]

    username = models.CharField(max_length=255, unique=True)
    post = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    communications = models.CharField(max_length=255)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)
    role = models.CharField(max_length=255, choices=CATEGORY_TYPES, default=default)
    email = models.EmailField(max_length=255, unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.name