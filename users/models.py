from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db import models


# Кастомный менеджер пользователя
class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email обязателен')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


# Кастомная модель пользователя
class User(AbstractUser):
    username = None  # убираем username
    email = models.EmailField(unique=True, verbose_name="Электронная почта")

    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True, verbose_name="Аватар")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Телефон")
    country = models.CharField(max_length=50, blank=True, null=True, verbose_name="Страна")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  # при создании суперпользователя требуется только email и пароль

    objects = UserManager()

    def __str__(self):
        return self.email

