# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-27 20:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('izettle', '0004_variant'),
    ]

    operations = [
        migrations.CreateModel(
            name='SKU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='izettle.Product')),
                ('variant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='izettle.Variant')),
            ],
        ),
    ]