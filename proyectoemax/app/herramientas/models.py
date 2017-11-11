# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class herramienta(models.Model):
    nombre = models.CharField(max_length=50)
    existencias = models.PositiveIntegerField()
    preciounitario = models.FloatField(default=0.0)
    imagen = models.ImageField(blank=True)

    def __str__(self):
        return self.nombre
