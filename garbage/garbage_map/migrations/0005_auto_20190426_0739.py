# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-26 07:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garbage_map', '0004_auto_20190425_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dot',
            name='name',
            field=models.CharField(default='', max_length=120, verbose_name='NAME222'),
        ),
    ]
