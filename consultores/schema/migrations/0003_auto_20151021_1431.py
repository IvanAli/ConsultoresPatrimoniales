# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0002_auto_20151021_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agente',
            name='sexo',
            field=models.CharField(choices=[(None, '-'), ('M', 'Mujer'), ('H', 'Hombre'), ('O', 'Otro')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='sexo',
            field=models.CharField(choices=[(None, '-'), ('M', 'Mujer'), ('H', 'Hombre'), ('O', 'Otro')], default='M', max_length=1),
        ),
    ]
