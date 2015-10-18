# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0002_auto_20151018_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='comparativa',
            name='fechaConclusion',
            field=models.DateTimeField(blank=True, verbose_name='fecha concluida', null=True),
        ),
        migrations.AddField(
            model_name='comparativa',
            name='fechaCreacion',
            field=models.DateTimeField(auto_now_add=True, verbose_name='fecha creada', null=True),
        ),
        migrations.AddField(
            model_name='comparativa',
            name='fechaEnvio',
            field=models.DateTimeField(blank=True, verbose_name='fecha de envio', null=True),
        ),
        migrations.AlterField(
            model_name='agente',
            name='edad',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='edad',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='tiposeguro',
            name='idTipoSeguro',
            field=models.CharField(choices=[('AP', 'Automoviles y pickups'), ('C', 'Camiones'), ('R', 'Remolques, cajas secas y adaptaciones en general'), ('G', 'Gastos medicos mayores'), ('V', 'Vida'), ('H', 'Hogares'), ('I', 'Inversion'), ('E', 'Empresas'), ('EC', 'Equipo de contratistas'), ('T', 'Transportes'), ('ESP', 'Especializados')], max_length=3, primary_key=True, serialize=False),
        ),
    ]
