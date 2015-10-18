# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agente',
            fields=[
                ('idUsuario', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=40)),
                ('apellidoPaterno', models.CharField(max_length=20)),
                ('apellidoMaterno', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=60)),
                ('telefonoLada', models.CharField(max_length=3)),
                ('telefono', models.CharField(max_length=7)),
                ('calle', models.CharField(max_length=50)),
                ('numeroExt', models.IntegerField()),
                ('numeroInt', models.IntegerField(blank=True)),
                ('colonia', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=25)),
                ('estado', models.CharField(max_length=25)),
                ('codigoPostal', models.IntegerField()),
                ('usuario', models.CharField(max_length=30)),
                ('contrasena', models.CharField(max_length=30)),
                ('claveAgente', models.IntegerField()),
                ('cuentaBancaria', models.CharField(max_length=34)),
                ('banco', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Aseguradora',
            fields=[
                ('idAseguradora', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('sitioWeb', models.TextField(blank=True)),
                ('telefonoLada', models.CharField(max_length=3)),
                ('telefono', models.CharField(max_length=7)),
                ('calle', models.CharField(max_length=50)),
                ('numeroExt', models.IntegerField()),
                ('numeroInt', models.IntegerField(blank=True)),
                ('colonia', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=25)),
                ('estado', models.CharField(max_length=25)),
                ('codigoPostal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AsignacionComision',
            fields=[
                ('idAsignacion', models.AutoField(serialize=False, primary_key=True)),
                ('fechaAsignacion', models.DateTimeField(verbose_name=b'fecha de asignacion')),
                ('porcentaje', models.DecimalField(max_digits=3, decimal_places=1)),
                ('aseguradora', models.ForeignKey(to='schema.Aseguradora')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('idUsuario', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=40)),
                ('apellidoPaterno', models.CharField(max_length=20)),
                ('apellidoMaterno', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=60)),
                ('telefonoLada', models.CharField(max_length=3)),
                ('telefono', models.CharField(max_length=7)),
                ('calle', models.CharField(max_length=50)),
                ('numeroExt', models.IntegerField()),
                ('numeroInt', models.IntegerField(blank=True)),
                ('colonia', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=25)),
                ('estado', models.CharField(max_length=25)),
                ('codigoPostal', models.IntegerField()),
                ('usuario', models.CharField(max_length=30)),
                ('contrasena', models.CharField(max_length=30)),
                ('linkRegistroRFC', models.URLField()),
                ('linkComprobanteDomicilio', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cobertura',
            fields=[
                ('idCobertura', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
                ('porcentajeCobertura', models.DecimalField(max_digits=3, decimal_places=1)),
            ],
        ),
        migrations.CreateModel(
            name='Comision',
            fields=[
                ('idComision', models.AutoField(serialize=False, primary_key=True)),
                ('cantidadComision', models.DecimalField(max_digits=3, decimal_places=1)),
                ('fechaDeposito', models.DateTimeField(null=True)),
                ('asignacionComision', models.ForeignKey(to='schema.AsignacionComision')),
            ],
        ),
        migrations.CreateModel(
            name='Comparativa',
            fields=[
                ('idComparativa', models.AutoField(serialize=False, primary_key=True)),
                ('numeroCotizaciones', models.IntegerField()),
                ('fechaCreacion', models.DateTimeField(verbose_name=b'fecha creada')),
                ('fechaConclusion', models.DateTimeField(verbose_name=b'fecha concluida')),
                ('fechaEnvio', models.DateTimeField(verbose_name=b'fecha de envio')),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('idContacto', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=40)),
                ('apellidoPaterno', models.CharField(max_length=20)),
                ('apellidoMaterno', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=60)),
                ('telefonoLada', models.CharField(max_length=3)),
                ('telefono', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('idCotizacion', models.AutoField(serialize=False, primary_key=True)),
                ('costo', models.DecimalField(max_digits=3, decimal_places=1)),
                ('fechaCreacion', models.DateTimeField(verbose_name=b'fecha creada')),
                ('formaPago', models.IntegerField(default=12, choices=[(12, b'Anual'), (6, b'Semestral'), (3, b'Trimestral')])),
                ('aseguradora', models.ForeignKey(to='schema.Aseguradora')),
                ('comparativa', models.ForeignKey(to='schema.Comparativa')),
            ],
        ),
        migrations.CreateModel(
            name='Dato',
            fields=[
                ('idDato', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OrdenServicio',
            fields=[
                ('idServicio', models.AutoField(serialize=False, primary_key=True)),
                ('fechaServicio', models.DateTimeField(verbose_name=b'fecha de servicio')),
                ('agente', models.ForeignKey(to='schema.Agente')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('idPago', models.AutoField(serialize=False, primary_key=True)),
                ('cantidad', models.DecimalField(max_digits=3, decimal_places=1)),
                ('fechaPago', models.DateTimeField(verbose_name=b'fecha de pago')),
            ],
        ),
        migrations.CreateModel(
            name='Poliza',
            fields=[
                ('idPoliza', models.AutoField(serialize=False, primary_key=True)),
                ('primaNeta', models.DecimalField(max_digits=3, decimal_places=1)),
                ('fechaEmision', models.DateTimeField(verbose_name=b'fecha emitida')),
                ('fechaInicio', models.DateTimeField(verbose_name=b'fecha de inicio')),
                ('fechaFin', models.DateTimeField(verbose_name=b'fecha de fin')),
                ('endosoBeneficiario', models.CharField(max_length=50)),
                ('linkCaratulaPDF', models.URLField()),
                ('comision', models.ForeignKey(to='schema.Comision')),
                ('servicio', models.ForeignKey(to='schema.OrdenServicio')),
            ],
        ),
        migrations.CreateModel(
            name='TipoSeguro',
            fields=[
                ('idTipoSeguro', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ClienteFisica',
            fields=[
                ('cliente_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='schema.Cliente')),
                ('calleFact', models.CharField(max_length=50)),
                ('numeroExtFact', models.IntegerField()),
                ('numeroIntFact', models.IntegerField(blank=True)),
                ('coloniaFact', models.CharField(max_length=50)),
                ('ciudadFact', models.CharField(max_length=25)),
                ('estadoFact', models.CharField(max_length=25)),
                ('codigoPostalFact', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=('schema.cliente',),
        ),
        migrations.CreateModel(
            name='ClienteMoral',
            fields=[
                ('cliente_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='schema.Cliente')),
                ('razonSocial', models.CharField(max_length=100)),
                ('linkActaConstitutiva', models.URLField()),
                ('linkIdRepresentante', models.URLField()),
            ],
            options={
                'abstract': False,
            },
            bases=('schema.cliente',),
        ),
        migrations.AddField(
            model_name='ordenservicio',
            name='cliente',
            field=models.ForeignKey(to='schema.Cliente'),
        ),
        migrations.AddField(
            model_name='comparativa',
            name='tipoSeguro',
            field=models.ForeignKey(to='schema.TipoSeguro'),
        ),
        migrations.AddField(
            model_name='asignacioncomision',
            name='tipoSeguro',
            field=models.ForeignKey(to='schema.TipoSeguro'),
        ),
    ]
