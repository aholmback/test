from rest_framework import serializers
from . import models


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Test
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
