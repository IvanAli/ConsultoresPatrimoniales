# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0002_auto_20151026_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agente',
            name='sexo',
            field=models.CharField(max_length=1, choices=[(None, '-'), ('M', 'Mujer'), ('H', 'Hombre'), ('O', 'Otro')]),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='sexo',
            field=models.CharField(max_length=1, choices=[(None, '-'), ('M', 'Mujer'), ('H', 'Hombre'), ('O', 'Otro')]),
        ),
    ]
