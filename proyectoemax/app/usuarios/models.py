# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class usuario(models.Model):
    nombre = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
