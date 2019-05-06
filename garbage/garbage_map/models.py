# coding=utf-8
from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 120, default = '', verbose_name = 'Название категории')
    image = models.ImageField(upload_to='photo', blank = True, verbose_name = 'Изображение')
    
    def __unicode__(self):
        return self.name

class Dot(models.Model):
    name = models.CharField(max_length = 120, default = '', verbose_name = 'Название пункта')
    description = models.CharField(max_length = 120, default = '',  verbose_name = 'Описание')
    x = models.FloatField(default = 0.0, verbose_name = 'Координата х')
    y = models.FloatField(default = 0.0, verbose_name = 'Координата у')
    working_hours = models.TextField(default = '', verbose_name = 'Время и часы работы')
    category = models.ManyToManyField(Category, verbose_name = 'Категория мусора')
    image = models.ImageField(upload_to='photo_garbage', blank = True, verbose_name = 'Изображение')
    
    def __unicode__(self):
        return self.name



