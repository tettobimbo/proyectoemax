# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 06:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materiales', '0002_material_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='cantidad',
            field=models.PositiveIntegerField(),
        ),
    ]
