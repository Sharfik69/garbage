from __future__ import unicode_literals

from django.db import models

class Dots(models.Model):
    Group_user = models.CharField(max_length = 15, default = '')

    Subject = models.CharField(max_length = 120)

    def __str__(self):
        return self.Subject