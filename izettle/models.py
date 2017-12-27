from django.db import models


class Test(models.Model):
    field = models.CharField(max_length=255)
    product = models.ForeignKey('izettle.Product', null=True)


class Product(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
