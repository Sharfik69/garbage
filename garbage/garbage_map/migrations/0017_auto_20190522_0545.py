# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-22 05:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garbage_map', '0016_category_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]