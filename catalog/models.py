from django.db import models
from django.utils import timezone

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    """
    Создание модели в БД "Category", прямая связь с таблицей "Product" через "category"
    """
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    """
    Создание модели в БД "Product", прямая связь с таблицей "Category" через "category"
    """
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='catalog/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.FloatField(verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    updated_at = models.DateTimeField(verbose_name='Дата изменения', **NULLABLE)
    # manufactured_at = models.DateTimeField(default=timezone.now(), verbose_name='Дата производства продукта')

    def __str__(self):
        return f"{self.name} ({self.price})"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
