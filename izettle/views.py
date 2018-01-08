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
    allSKUs = Product.objects.values('id', 'name', 'sku', 'sku__variant__name', 'sku__price')
    products = Product.objects.values('id', 'name')
    context = []

    for product in products:
        variantsArr = []
        for sku in allSKUs:
            if sku['sku'] is not None and sku['id']==product['id']:
                variantsArr.append({'sku_id': sku['sku'], 'variant_name': sku['sku__variant__name'], 'price': sku['sku__price']})
        if len(variantsArr) > 0:
            context.append({'id': product['id'], 'name': product['name'], 'variants': variantsArr})

    #context = list(context)
    #print(context)

    return JsonResponse(context, safe=False)

