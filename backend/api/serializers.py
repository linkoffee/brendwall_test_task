from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор продуктов."""

    class Meta:
        model = Product
        fields = '__all__'

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError('Цена не может быть меньше 0!')
        return value
