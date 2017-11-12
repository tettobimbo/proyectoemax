# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class RetornoDeHerramientas(models.Model):
    fechaentrega = models.DateField()
    direccion = models.CharField(max_length=50)
    descripcion= models.CharField(max_length=50)
    solicitante = models.CharField(max_length=50)

def __str__(self):
    return self.direccion
