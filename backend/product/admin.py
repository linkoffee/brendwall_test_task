from django.contrib import admin

from .models import Product

admin.site.empty_value_display = 'пусто'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Админ-модель продукта."""

    list_display = ('name', 'description', 'price')
    search_fields = ('name',)
    list_filter = ('name', 'price')
