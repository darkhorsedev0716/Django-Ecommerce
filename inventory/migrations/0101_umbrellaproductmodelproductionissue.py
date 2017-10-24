# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-25 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0100_material_name_cz'),
    ]

    operations = [
        migrations.CreateModel(
            name='UmbrellaProductModelProductionIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=200)),
                ('name_cz', models.CharField(blank=True, max_length=200, null=True)),
                ('note_en', models.TextField()),
                ('note_cz', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/production/notes/images/%Y/%m/%d')),
                ('umbrella_product', models.ManyToManyField(blank=True, to='inventory.UmbrellaProduct')),
                ('umbrella_product_model', models.ManyToManyField(blank=True, to='inventory.UmbrellaProductModel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]