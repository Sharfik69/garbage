# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-22 03:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garbage_map', '0014_dot_addres'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u043e\u0442\u0445\u043e\u0434\u043e\u0432', 'verbose_name_plural': '\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u043e\u0442\u0445\u043e\u0434\u043e\u0432'},
        ),
        migrations.AlterModelOptions(
            name='dot',
            options={'verbose_name': '\u043f\u0443\u043d\u043a\u0442 \u043f\u0435\u0440\u0435\u0440\u0430\u0431\u043e\u0442\u043a\u0438', 'verbose_name_plural': '\u043f\u0443\u043d\u043a\u0442\u044b \u043f\u0435\u0440\u0435\u0440\u0430\u0431\u043e\u0442\u043a\u0438'},
        ),
    ]
