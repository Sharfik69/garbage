from __future__ import unicode_literals

from django.db import models

class Dots(models.Model):
    Subject = models.CharField(max_length = 120, default = '')
    dot_x = models.FloatField(default = 0.0)
    dot_y = models.FloatField(default = 0.0)


def __str__(self):
    return self.Subject
