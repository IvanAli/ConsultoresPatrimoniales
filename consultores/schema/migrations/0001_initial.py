# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('email', models.EmailField(null=True, max_length=254, blank=True)),
                ('edad', models.PositiveSmallIntegerField(null=True)),
                ('sexo', models.CharField(default=None, choices=[(None, '-'), ('M', 'Mujer'), ('H', 'Hombre'), ('O', 'Otro')], max_length=1)),
                ('rfc', models.CharField(null=True, max_length=13)),
                ('telefonoLada', models.CharField(null=True, max_length=3)),
                ('telefono', models.CharField(null=True, max_length=7)),
                ('calle', models.CharField(null=True, max_length=50, blank=True)),
                ('numeroExt', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('numeroInt', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('colonia', models.CharField(null=True, max_length=40, blank=True)),
                ('ciudad', models.CharField(null=True, max_length=30, blank=True)),
                ('estado', models.CharField(null=True, max_length=19, blank=True)),
                ('codigoPostal', models.CharField(null=True, max_length=5, blank=True)),
                ('claveAgente', models.IntegerField(null=True, blank=True)),
                ('cuentaBancaria', models.CharField(null=True, max_length=34)),
                ('banco', models.CharField(null=True, max_length=30)),
                ('userAgente', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Aseguradora',
            fields=[
                ('idAseguradora', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(null=True, max_length=50)),
                ('sitioWeb', models.URLField(null=True, blank=True)),
                ('telefonoLada', models.CharField(null=True, max_length=3)),
                ('telefono', models.CharField(null=True, max_length=7)),
                ('calle', models.CharField(null=True, max_length=50, blank=True)),
                ('numeroExt', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('numeroInt', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('colonia', models.CharField(null=True, max_length=40, blank=True)),
                ('ciudad', models.CharField(null=True, max_length=30, blank=True)),
                ('estado', models.CharField(null=True, max_length=19, blank=True)),
                ('codigoPostal', models.CharField(null=True, max_length=5, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AsignacionComision',
            fields=[
                ('idAsignacion', models.AutoField(primary_key=True, serialize=False)),
                ('fechaAsignacion', models.DateTimeField(verbose_name='fecha de asignacion')),
                ('porcentaje', models.DecimalField(null=True, decimal_places=2, max_digits=4)),
                ('aseguradora', models.ForeignKey(null=True, to='schema.Aseguradora')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('email', models.EmailField(null=True, max_length=254, blank=True)),
                ('edad', models.PositiveSmallIntegerField(null=True)),
                ('sexo', models.CharField(default=None, choices=[(None, '-'), ('M', 'Mujer'), ('H', 'Hombre'), ('O', 'Otro')], max_length=1)),
                ('rfc', models.CharField(null=True, max_length=13)),
                ('telefonoLada', models.CharField(null=True, max_length=3)),
                ('telefono', models.CharField(null=True, max_length=7)),
                ('calle', models.CharField(null=True, max_length=50, blank=True)),
                ('numeroExt', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('numeroInt', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('colonia', models.CharField(null=True, max_length=40, blank=True)),
                ('ciudad', models.CharField(null=True, max_length=30, blank=True)),
                ('estado', models.CharField(null=True, max_length=19, blank=True)),
                ('codigoPostal', models.CharField(null=True, max_length=5, blank=True)),
                ('nombre', models.CharField(null=True, max_length=40)),
                ('apellidoPaterno', models.CharField(null=True, max_length=30)),
                ('apellidoMaterno', models.CharField(null=True, max_length=30)),
                ('linkRegistroRFC', models.URLField(null=True)),
                ('linkComprobanteDomicilio', models.URLField(null=True)),
                ('calleFact', models.CharField(null=True, max_length=50)),
                ('numeroExtFact', models.PositiveSmallIntegerField(null=True)),
                ('numeroIntFact', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('coloniaFact', models.CharField(null=True, max_length=40)),
                ('ciudadFact', models.CharField(null=True, max_length=30)),
                ('estadoFact', models.CharField(null=True, max_length=19)),
                ('codigoPostalFact', models.CharField(null=True, max_length=5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cobertura',
            fields=[
                ('idCobertura', models.AutoField(primary_key=True, serialize=False)),
                ('nombreCobertura', models.CharField(null=True, max_length=50)),
                ('descripcion', models.TextField(null=True)),
                ('porcentajeCobertura', models.DecimalField(null=True, decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='CoberturasRequeridas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('cobertura', models.ForeignKey(null=True, to='schema.Cobertura')),
            ],
        ),
        migrations.CreateModel(
            name='CoberturasUtilizadas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('cobertura', models.ForeignKey(null=True, to='schema.Cobertura')),
            ],
        ),
        migrations.CreateModel(
            name='Comision',
            fields=[
                ('idComision', models.AutoField(primary_key=True, serialize=False)),
                ('cantidadComision', models.DecimalField(null=True, decimal_places=2, max_digits=11)),
                ('fechaDeposito', models.DateTimeField(null=True)),
                ('agente', models.ForeignKey(null=True, to='schema.Agente')),
            ],
        ),
        migrations.CreateModel(
            name='Comparativa',
            fields=[
                ('idComparativa', models.AutoField(primary_key=True, serialize=False)),
                ('numeroCotizaciones', models.PositiveIntegerField(null=True)),
                ('fechaCreacion', models.DateTimeField(null=True, auto_now_add=True, verbose_name='fecha creada')),
                ('fechaConclusion', models.DateTimeField(null=True, blank=True, verbose_name='fecha concluida')),
                ('fechaEnvio', models.DateTimeField(null=True, blank=True, verbose_name='fecha de envio')),
                ('agente', models.ForeignKey(null=True, to='schema.Agente')),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('idContacto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(null=True, max_length=40)),
                ('apellidoPaterno', models.CharField(null=True, max_length=30)),
                ('apellidoMaterno', models.CharField(null=True, max_length=30)),
                ('email', models.EmailField(null=True, max_length=254)),
                ('telefonoLada', models.CharField(null=True, max_length=3, blank=True)),
                ('telefono', models.CharField(null=True, max_length=7, blank=True)),
                ('aseguradora', models.ForeignKey(null=True, to='schema.Aseguradora')),
            ],
        ),
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('idCotizacion', models.AutoField(primary_key=True, serialize=False)),
                ('costo', models.DecimalField(null=True, decimal_places=2, max_digits=11)),
                ('fechaCreacion', models.DateTimeField(null=True, verbose_name='fecha creada')),
                ('formaPago', models.IntegerField(default=12, choices=[(12, 'Anual'), (6, 'Semestral'), (3, 'Trimestral')], null=True)),
                ('aseguradora', models.ForeignKey(null=True, to='schema.Aseguradora')),
                ('comparativa', models.ForeignKey(null=True, to='schema.Comparativa')),
            ],
        ),
        migrations.CreateModel(
            name='Dato',
            fields=[
                ('idDato', models.AutoField(primary_key=True, serialize=False)),
                ('nombreDato', models.CharField(null=True, max_length=50)),
                ('tipoDato', models.CharField(null=True, max_length=50)),
                ('descripcion', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DatosNecesitados',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('dato', models.ForeignKey(null=True, to='schema.Dato')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenServicio',
            fields=[
                ('idServicio', models.AutoField(primary_key=True, serialize=False)),
                ('fechaServicio', models.DateTimeField(auto_now_add=True, verbose_name='fecha de servicio')),
                ('fechaConclusion', models.DateTimeField(null=True, blank=True)),
                ('agente', models.ForeignKey(null=True, to='schema.Agente')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('idPago', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.DecimalField(null=True, decimal_places=2, max_digits=11)),
                ('fechaPago', models.DateTimeField(null=True, verbose_name='fecha de pago')),
                ('numeroPago', models.PositiveSmallIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Poliza',
            fields=[
                ('idPoliza', models.AutoField(primary_key=True, serialize=False)),
                ('primaNeta', models.DecimalField(null=True, decimal_places=2, max_digits=11)),
                ('fechaEmision', models.DateTimeField(null=True, verbose_name='fecha emitida')),
                ('fechaInicio', models.DateTimeField(null=True, verbose_name='fecha de inicio')),
                ('fechaFin', models.DateTimeField(null=True, verbose_name='fecha de fin')),
                ('endosoBeneficiario', models.CharField(null=True, max_length=50)),
                ('linkCaratulaPDF', models.URLField(null=True)),
                ('agente', models.ForeignKey(null=True, to='schema.Agente')),
                ('aseguradora', models.ForeignKey(null=True, to='schema.Aseguradora')),
            ],
        ),
        migrations.CreateModel(
            name='SegurosOfertados',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('aseguradora', models.ForeignKey(to='schema.Aseguradora')),
            ],
        ),
        migrations.CreateModel(
            name='TipoSeguro',
            fields=[
                ('nombre', models.CharField(null=True, max_length=50)),
                ('idTipoSeguro', models.CharField(primary_key=True, choices=[('AP', 'Automoviles y pickups'), ('C', 'Camiones'), ('R', 'Remolques, cajas secas y adaptaciones en general'), ('G', 'Gastos medicos mayores'), ('V', 'Vida'), ('H', 'Hogares'), ('I', 'Inversion'), ('E', 'Empresas'), ('EC', 'Equipo de contratistas'), ('T', 'Transportes'), ('ESP', 'Especializados')], max_length=3, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ClienteFisico',
            fields=[
                ('cliente_ptr', models.OneToOneField(serialize=False, auto_created=True, primary_key=True, to='schema.Cliente', parent_link=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('schema.cliente',),
        ),
        migrations.CreateModel(
            name='ClienteMoral',
            fields=[
                ('cliente_ptr', models.OneToOneField(serialize=False, auto_created=True, primary_key=True, to='schema.Cliente', parent_link=True)),
                ('razonSocial', models.CharField(null=True, max_length=100)),
                ('linkActaConstitutiva', models.URLField(null=True)),
                ('linkIdRepresentante', models.URLField(null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('schema.cliente',),
        ),
        migrations.AddField(
            model_name='segurosofertados',
            name='seguro',
            field=models.ForeignKey(to='schema.TipoSeguro'),
        ),
        migrations.AddField(
            model_name='poliza',
            name='cliente',
            field=models.ForeignKey(null=True, to='schema.Cliente'),
        ),
        migrations.AddField(
            model_name='poliza',
            name='comision',
            field=models.ForeignKey(null=True, to='schema.Comision'),
        ),
        migrations.AddField(
            model_name='pago',
            name='poliza',
            field=models.ForeignKey(null=True, to='schema.Poliza'),
        ),
        migrations.AddField(
            model_name='ordenservicio',
            name='cliente',
            field=models.ForeignKey(null=True, to='schema.Cliente'),
        ),
        migrations.AddField(
            model_name='ordenservicio',
            name='comparativa',
            field=models.ForeignKey(null=True, to='schema.Comparativa'),
        ),
        migrations.AddField(
            model_name='ordenservicio',
            name='poliza',
            field=models.ForeignKey(null=True, to='schema.Poliza'),
        ),
        migrations.AddField(
            model_name='ordenservicio',
            name='tipoSeguro',
            field=models.ForeignKey(null=True, to='schema.TipoSeguro'),
        ),
        migrations.AddField(
            model_name='datosnecesitados',
            name='seguro',
            field=models.ForeignKey(null=True, to='schema.TipoSeguro'),
        ),
        migrations.AddField(
            model_name='comparativa',
            name='cliente',
            field=models.ForeignKey(null=True, to='schema.Cliente'),
        ),
        migrations.AddField(
            model_name='coberturasutilizadas',
            name='poliza',
            field=models.ForeignKey(null=True, to='schema.Poliza'),
        ),
        migrations.AddField(
            model_name='coberturasrequeridas',
            name='comparativa',
            field=models.ForeignKey(null=True, to='schema.Comparativa'),
        ),
        migrations.AddField(
            model_name='cobertura',
            name='seguro',
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
    ]
