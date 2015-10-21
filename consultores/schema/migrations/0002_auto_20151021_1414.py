# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agente',
            name='sexo',
            field=models.CharField(null=True, default=None, choices=[(None, '-'), ('M', 'Mujer'), ('H', 'Hombre'), ('O', 'Otro')], max_length=1),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='sexo',
            field=models.CharField(null=True, default=None, choices=[(None, '-'), ('M', 'Mujer'), ('H', 'Hombre'), ('O', 'Otro')], max_length=1),
        ),
    ]
