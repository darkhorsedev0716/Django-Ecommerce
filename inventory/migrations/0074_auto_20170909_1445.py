# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-09 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0073_auto_20170908_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocklocationitem',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]