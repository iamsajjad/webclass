
import os
from django.conf import settings
from django.db import models

# Create your models here.

class UserSettings(models.Model):

    id         = models.AutoField(primary_key=True)
    author     = models.CharField(max_length=100, default='admin')
    privilege  = models.CharField(max_length=100, default='user')

    def __unicode__(self):
        return self.id

    class Meta:
        ordering = ('id',)
        verbose_name = 'Settings'
        verbose_name_plural = 'Settings'

    def __str__(self):
        return str('{0} : {1}'.format(
            self.id,
            self.author))

