from django.contrib import admin
from .models import Category, Product, Contact

# Регистрация категории с нужным отображением
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')   # выводим id и name
    search_fields = ('name',)       # поиск по имени

# Регистрация продукта с нужным отображением и фильтрацией
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')  # id, name, price, category
    list_filter = ('category',)                         # фильтрация по категории
    search_fields = ('name', 'description')            # поиск по name и description

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address')
    search_fields = ('name', 'email', 'phone')
