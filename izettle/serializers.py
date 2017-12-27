from rest_framework import serializers
from . import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'

class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Variant
        fields = '__all__'

class SKUSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    variant = VariantSerializer(required=False)

    class Meta:
        model = models.SKU
        fields = '__all__'


class TestSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = models.Test
        fields = '__all__'
