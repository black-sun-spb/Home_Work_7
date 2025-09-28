from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None  # убираем username
    email = models.EmailField(unique=True, verbose_name="Электронная почта")

    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True, verbose_name="Аватар")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Телефон")
    country = models.CharField(max_length=50, blank=True, null=True, verbose_name="Страна")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  # при создании superuser будет требоваться только email и пароль

    def __str__(self):
        return self.email
