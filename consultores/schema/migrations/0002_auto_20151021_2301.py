# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cobertura',
            name='tipoSeguro',
            field=models.ForeignKey(to='schema.TipoSeguro', null=True),
        ),
        migrations.AlterField(
            model_name='tiposeguro',
            name='aseguradora',
            field=models.ForeignKey(to='schema.Aseguradora', null=True),
        ),
    ]
