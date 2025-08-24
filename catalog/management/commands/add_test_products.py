from django.core.management.base import BaseCommand
from catalog.models import Category, Product
from django.utils import timezone


class Command(BaseCommand):
    help = "Удаляет все существующие продукты и категории, добавляет тестовые данные"

    def handle(self, *args, **options):
        # Удаляем все данные
        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write(self.style.WARNING("Все данные удалены"))

        # Создаём категории
        cat1 = Category.objects.create(name="Электроника", description="Гаджеты и устройства")
        cat2 = Category.objects.create(name="Книги", description="Различные книги и учебники")
        cat3 = Category.objects.create(name="Одежда", description="Мужская и женская одежда")

        # Создаём продукты
        Product.objects.create(
            name="Смартфон",
            description="Современный смартфон",
            category=cat1,
            price=50000,
            created_at=timezone.now(),
            updated_at=timezone.now()
        )
        Product.objects.create(
            name="Ноутбук",
            description="Мощный ноутбук",
            category=cat1,
            price=80000,
            created_at=timezone.now(),
            updated_at=timezone.now()
        )
        Product.objects.create(
            name="Роман 'Война и мир'",
            description="Классическая литература",
            category=cat2,
            price=1200,
            created_at=timezone.now(),
            updated_at=timezone.now()
        )
        Product.objects.create(
            name="Футболка",
            description="Хлопковая футболка",
            category=cat3,
            price=800,
            created_at=timezone.now(),
            updated_at=timezone.now()
        )

        self.stdout.write(self.style.SUCCESS("Тестовые продукты успешно добавлены"))
