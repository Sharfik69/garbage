from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 120, default = '')
    
    def __unicode__(self):
        return self.name

class Dot(models.Model):
    name = models.CharField(max_length = 120, default = '')
    description = models.CharField(max_length = 120, default = '')
    x = models.FloatField(default = 0.0)
    y = models.FloatField(default = 0.0)
    category = models.ManyToManyField(Category)
    
    def __unicode__(self):
        return self.name
