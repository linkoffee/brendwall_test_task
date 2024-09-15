from django.db import models

from .constants import (
    CHAR_OUTPUT_LIMIT,
    MAX_PRODUCT_NAME_LEN,
    PRICE_DECIMAL_PLACES,
    PRICE_MAX_DIGITS,
)


class Product(models.Model):
    """Модель продукта."""

    name = models.CharField(
        unique=True,
        max_length=MAX_PRODUCT_NAME_LEN
    )
    description = models.TextField()
    price = models.DecimalField(
        max_digits=PRICE_MAX_DIGITS,
        decimal_places=PRICE_DECIMAL_PLACES
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name[:CHAR_OUTPUT_LIMIT]
