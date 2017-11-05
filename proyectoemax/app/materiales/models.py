# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class material(models.Model):
        nombre = models.CharField(max_length=50)
        cantidad = models.IntegerField()
        medida= models.CharField(max_length=15)
        preciounitario= models.FloatField(default=0.0)

        def __str__(self):
            return self.nombre
