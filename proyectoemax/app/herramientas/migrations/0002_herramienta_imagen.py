# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 23:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herramientas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='herramienta',
            name='imagen',
            field=models.ImageField(blank=True, upload_to=b''),
        ),
    ]