# coding=utf-8
from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 120, default = '', verbose_name = 'Название категории')
    name_html = models.CharField(max_length = 120, default = '', blank=True, verbose_name = 'Название категории (html)')
    image = models.ImageField(upload_to='photo', blank = True, verbose_name = 'Изображение')
    icon_class = models.CharField(max_length=100, default = '', verbose_name='Класс иконки')
    order = models.IntegerField(default = 0, null = False)
    
    class Meta:
        verbose_name = u'категория отходов'
        verbose_name_plural = u'категории отходов'
    
    def __unicode__(self):
        return self.name


class Dot(models.Model):
    name = models.CharField(max_length = 512, default = '', verbose_name = 'Название пункта')
    description = models.TextField(default = '',  verbose_name = 'Описание')
    addres = models.CharField(max_length = 512, default = '',  verbose_name = 'Адрес')
    phone = models.TextField(default = '', verbose_name = 'Телефон')
    x = models.FloatField(verbose_name = 'Координата х')
    y = models.FloatField(verbose_name = 'Координата у')
    working_hours = models.TextField(default = '', verbose_name = 'Время и часы работы')
    categories = models.ManyToManyField(Category, verbose_name = 'Категория мусора')
    image = models.ImageField(upload_to = 'photo_garbage', blank = True, verbose_name = 'Изображение')

    class Meta:
        verbose_name = u'пункт переработки'
        verbose_name_plural = u'пункты переработки'
    
    def __unicode__(self):
        return self.name



