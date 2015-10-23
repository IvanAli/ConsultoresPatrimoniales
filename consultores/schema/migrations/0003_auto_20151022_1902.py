# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0002_auto_20151021_2301'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsignacionComision',
            fields=[
                ('idAsignacion', models.AutoField(primary_key=True, serialize=False)),
                ('fechaAsignacion', models.DateTimeField(verbose_name='fecha de asignacion')),
                ('porcentaje', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('aseguradora', models.ForeignKey(null=True, to='schema.Aseguradora')),
            ],
        ),
        migrations.CreateModel(
            name='Comision',
            fields=[
                ('idComision', models.AutoField(primary_key=True, serialize=False)),
                ('cantidadComision', models.DecimalField(decimal_places=2, max_digits=11, null=True)),
                ('fechaDeposito', models.DateTimeField(null=True)),
                ('agente', models.ForeignKey(null=True, to='schema.Agente')),
            ],
        ),
        migrations.CreateModel(
            name='Comparativa',
            fields=[
                ('idComparativa', models.AutoField(primary_key=True, serialize=False)),
                ('numeroCotizaciones', models.PositiveIntegerField(null=True)),
                ('fechaCreacion', models.DateTimeField(verbose_name='fecha creada', null=True, auto_now_add=True)),
                ('fechaConclusion', models.DateTimeField(verbose_name='fecha concluida', null=True, blank=True)),
                ('fechaEnvio', models.DateTimeField(verbose_name='fecha de envio', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('idContacto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40, null=True)),
                ('apellidoPaterno', models.CharField(max_length=30, null=True)),
                ('apellidoMaterno', models.CharField(max_length=30, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('telefonoLada', models.CharField(max_length=3, null=True, blank=True)),
                ('telefono', models.CharField(max_length=7, null=True, blank=True)),
                ('aseguradora', models.ForeignKey(null=True, to='schema.Aseguradora')),
            ],
        ),
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('idCotizacion', models.AutoField(primary_key=True, serialize=False)),
                ('costo', models.DecimalField(decimal_places=2, max_digits=11, null=True)),
                ('fechaCreacion', models.DateTimeField(verbose_name='fecha creada', null=True)),
                ('formaPago', models.IntegerField(default=12, null=True, choices=[(12, 'Anual'), (6, 'Semestral'), (3, 'Trimestral')])),
                ('aseguradora', models.ForeignKey(null=True, to='schema.Aseguradora')),
                ('comparativa', models.ForeignKey(null=True, to='schema.Comparativa')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenServicio',
            fields=[
                ('idServicio', models.AutoField(primary_key=True, serialize=False)),
                ('fechaServicio', models.DateTimeField(verbose_name='fecha de servicio', auto_now_add=True)),
                ('fechaConclusion', models.DateTimeField(null=True, blank=True)),
                ('agente', models.ForeignKey(null=True, to='schema.Agente')),
                ('cliente', models.ForeignKey(null=True, to='schema.Cliente')),
                ('comparativa', models.OneToOneField(null=True, to='schema.Comparativa')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('idPago', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=11, null=True)),
                ('fechaPago', models.DateTimeField(verbose_name='fecha de pago', null=True)),
                ('numeroPago', models.PositiveSmallIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Poliza',
            fields=[
                ('idPoliza', models.AutoField(primary_key=True, serialize=False)),
                ('primaNeta', models.DecimalField(decimal_places=2, max_digits=11, null=True)),
                ('fechaEmision', models.DateTimeField(verbose_name='fecha emitida', null=True)),
                ('fechaInicio', models.DateTimeField(verbose_name='fecha de inicio', null=True)),
                ('fechaFin', models.DateTimeField(verbose_name='fecha de fin', null=True)),
                ('endosoBeneficiario', models.CharField(max_length=50, null=True)),
                ('linkCaratulaPDF', models.URLField(null=True)),
                ('comision', models.OneToOneField(null=True, to='schema.Comision')),
                ('cotizacion', models.OneToOneField(null=True, to='schema.Cotizacion')),
            ],
        ),
        migrations.AddField(
            model_name='pago',
            name='poliza',
            field=models.ForeignKey(null=True, to='schema.Poliza'),
        ),
        migrations.AddField(
            model_name='ordenservicio',
            name='poliza',
            field=models.OneToOneField(null=True, to='schema.Poliza'),
        ),
        migrations.AddField(
            model_name='ordenservicio',
            name='tipoSeguro',
            field=models.ForeignKey(null=True, to='schema.TipoSeguro'),
        ),
        migrations.AddField(
            model_name='asignacioncomision',
            name='comision',
            field=models.ForeignKey(null=True, to='schema.Comision'),
        ),
        migrations.AddField(
            model_name='asignacioncomision',
            name='tipoSeguro',
            field=models.ForeignKey(null=True, to='schema.TipoSeguro'),
        ),
        migrations.AddField(
            model_name='agente',
            name='clientes',
            field=models.ManyToManyField(through='schema.OrdenServicio', to='schema.Cliente'),
        ),
    ]
