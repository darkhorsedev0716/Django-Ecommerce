# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-20 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0009_auto_20170720_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='supplier_reference',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]