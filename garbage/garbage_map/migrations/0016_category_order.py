# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-22 04:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garbage_map', '0015_auto_20190522_0353'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='order',
            field=models.ImageField(default=0, upload_to=b''),
        ),
    ]