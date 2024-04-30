from django.contrib import admin

from catalog.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Регистрация класса "Product" из catalog/models.py в админ панель
    """
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Регистрация класса "Category" из models.py в админ панель
    """
    list_display = ('id', 'name',)
