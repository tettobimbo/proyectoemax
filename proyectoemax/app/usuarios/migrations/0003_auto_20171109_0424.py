# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 04:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_remove_usuario_nickname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='contrasena',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='nombre',
            new_name='username',
        ),
    ]