# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-29 07:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SalesOrderProducts',
            new_name='SalesOrderProduct',
        ),
    ]
