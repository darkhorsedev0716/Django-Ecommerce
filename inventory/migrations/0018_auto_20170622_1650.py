# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-22 14:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0017_auto_20170622_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.Relation'),
        ),
        migrations.DeleteModel(
            name='Supplier',
        ),
    ]
