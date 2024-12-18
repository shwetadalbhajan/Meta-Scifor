from rest_framework import serializers
from .models import Product
from decimal import Decimal

class ProductSerializer(serializers.ModelSerializer):
    price_with_discount = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['name', 'price', 'price_with_discount']

    def get_price_discount(self, obj):
        discount = Decimal('0.25')
        discounted_price = obj.price * (1 - discount)
        return round(discounted_price, 2)
