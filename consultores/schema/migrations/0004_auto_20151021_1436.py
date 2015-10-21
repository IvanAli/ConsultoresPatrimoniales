# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0003_auto_20151021_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='apellidoMaterno',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='apellidoPaterno',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='nombre',
        ),
    ]
