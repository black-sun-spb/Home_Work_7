import os
import django

# Указываем путь к настройкам Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")  # если settings.py в папке config
django.setup()

from catalog.models import Product
from users.models import User
from django.contrib.admin.models import LogEntry

# 1. Очистка логов админки от несуществующих пользователей
deleted_logs = LogEntry.objects.exclude(user__in=User.objects.all()).delete()
print(f"Удалено записей из django_admin_log: {deleted_logs[0]}")

# 2. Исправление продуктов без существующего владельца
admin_user = User.objects.filter(is_superuser=True).first()
if not admin_user:
    raise Exception("В базе нет суперпользователя!")

dangling_products = Product.objects.exclude(owner__in=User.objects.all())
print(f"Продуктов с несуществующим владельцем: {dangling_products.count()}")

for product in dangling_products:
    product.owner = admin_user
    product.save()
    print(f"Продукт '{product.name}' теперь принадлежит суперпользователю '{admin_user.email}'")

# Проверка
dangling_products = Product.objects.exclude(owner__in=User.objects.all())
print(f"Осталось продуктов с несуществующим владельцем: {dangling_products.count()}")

