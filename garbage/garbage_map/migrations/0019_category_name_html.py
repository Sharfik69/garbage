# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-06-04 06:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garbage_map', '0018_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_html',
            field=models.CharField(blank=True, default='', max_length=120, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 (html)'),
        ),
    ]
