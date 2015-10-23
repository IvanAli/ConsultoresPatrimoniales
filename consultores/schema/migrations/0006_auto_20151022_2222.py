# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0005_auto_20151022_2032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordenservicio',
            name='poliza',
        ),
        migrations.AddField(
            model_name='poliza',
            name='ordenServicio',
            field=models.OneToOneField(null=True, to='schema.OrdenServicio'),
        ),
    ]
