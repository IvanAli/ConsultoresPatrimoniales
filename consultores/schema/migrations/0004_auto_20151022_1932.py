# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0003_auto_20151022_1902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordenservicio',
            name='comparativa',
        ),
        migrations.AddField(
            model_name='comparativa',
            name='ordenServicio',
            field=models.ForeignKey(null=True, to='schema.OrdenServicio'),
        ),
    ]
