# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-27 20:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('izettle', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='izettle.Product'),
        ),
    ]
