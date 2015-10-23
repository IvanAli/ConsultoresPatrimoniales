# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0004_auto_20151022_1932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comparativa',
            name='numeroCotizaciones',
        ),
        migrations.AlterField(
            model_name='comparativa',
            name='ordenServicio',
            field=models.OneToOneField(to='schema.OrdenServicio', null=True),
        ),
    ]
