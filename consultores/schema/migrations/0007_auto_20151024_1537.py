# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0006_auto_20151022_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agente',
            name='edad',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='agente',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='agente',
            name='rfc',
            field=models.CharField(max_length=13, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='agente',
            name='sexo',
            field=models.CharField(default='M', max_length=1, choices=[(None, '-'), ('M', 'Mujer'), ('H', 'Hombre'), ('O', 'Otro')], blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='apellidoMaterno',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='apellidoPaterno',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='edad',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='rfc',
            field=models.CharField(max_length=13, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='sexo',
            field=models.CharField(default='M', max_length=1, choices=[(None, '-'), ('M', 'Mujer'), ('H', 'Hombre'), ('O', 'Otro')], blank=True),
        ),
    ]
