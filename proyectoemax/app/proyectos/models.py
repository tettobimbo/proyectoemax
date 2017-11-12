# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from app.materiales.models import material
from app.herramientas.models import herramienta
from django.db import models

# Create your models here.
class proyecto(models.Model):
    fechaentrega = models.DateField() #fecha de entrega de los materiales y las herramientas
    direccion = models.CharField(max_length=50)
    descripcion= models.CharField(max_length=50)
    encargado= models.CharField(max_length=50)
    totalmaterial=models.IntegerField()
    #Usuario = models.ForeignKey(usuario, null=True, blank=True, on_delete=models.CASCADE)
    Material=models.ManyToManyField(material, blank=True)
    Herramienta=models.ManyToManyField(herramienta, blank=True)

    def __str__(self):
        return self.direccion
