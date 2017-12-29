from django.http import JsonResponse
from .models import Product
from rest_framework import viewsets
from . import serializers, models


class TestViewSet(viewsets.ModelViewSet):
    queryset = models.Test.objects.all()
    serializer_class = serializers.TestSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class VariantViewSet(viewsets.ModelViewSet):
    queryset = models.Variant.objects.all()
    serializer_class = serializers.VariantSerializer


class SKUViewSet(viewsets.ModelViewSet):
    queryset = models.SKU.objects.all()
    serializer_class = serializers.SKUSerializer

def product(request):
    print(request)
    product = Product.objects.filter(pk=1).values('id', 'name', 'sku', 'sku__variant__name')

    context = list(product)
    return JsonResponse(context, safe=False)