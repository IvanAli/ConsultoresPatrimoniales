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
                ('email', models.EmailField(max_length=254)),
                ('edad', models.PositiveSmallIntegerField(null=True)),
                ('sexo', models.CharField(max_length=1, choices=[('M', 'Mujer'), ('H', 'Hombre'), ('O', 'Otro')])),
                ('rfc', models.CharField(blank=True, max_length=13)),
                ('telefonoLada', models.CharField(max_length=3)),
                ('telefono', models.CharField(max_length=7)),
                ('calle', models.CharField(blank=True, max_length=50)),
                ('numeroExt', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('numeroInt', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('colonia', models.CharField(blank=True, max_length=40)),
                ('ciudad', models.CharField(blank=True, max_length=30)),
                ('estado', models.CharField(blank=True, max_length=19)),
                ('codigoPostal', models.CharField(blank=True, max_length=5)),
                ('claveAgente', models.IntegerField(blank=True, null=True)),
                ('cuentaBancaria', models.CharField(blank=True, max_length=34)),
                ('banco', models.CharField(blank=True, max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Aseguradora',
            fields=[
                ('idAseguradora', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('sitioWeb', models.URLField(blank=True, null=True)),
                ('telefonoLada', models.CharField(max_length=3)),
                ('telefono', models.CharField(max_length=7)),
                ('calle', models.CharField(blank=True, max_length=50)),
                ('numeroExt', models.PositiveSmallIntegerField(blank=True)),
                ('numeroInt', models.PositiveSmallIntegerField(blank=True)),
                ('colonia', models.CharField(blank=True, max_length=40)),
                ('ciudad', models.CharField(blank=True, max_length=30)),
                ('estado', models.CharField(blank=True, max_length=19)),
                ('codigoPostal', models.CharField(blank=True, max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='AsignacionComision',
            fields=[
                ('idAsignacion', models.AutoField(primary_key=True, serialize=False)),
                ('fechaAsignacion', models.DateTimeField(verbose_name='fecha de asignacion', auto_now_add=True)),
                ('porcentaje', models.DecimalField(max_digits=4, decimal_places=2)),
                ('aseguradora', models.ForeignKey(to='schema.Aseguradora')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('email', models.EmailField(max_length=254)),
                ('edad', models.PositiveSmallIntegerField(null=True)),
                ('sexo', models.CharField(max_length=1, choices=[('M', 'Mujer'), ('H', 'Hombre'), ('O', 'Otro')])),
                ('rfc', models.CharField(blank=True, max_length=13)),
                ('telefonoLada', models.CharField(max_length=3)),
                ('telefono', models.CharField(max_length=7)),
                ('calle', models.CharField(blank=True, max_length=50)),
                ('numeroExt', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('numeroInt', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('colonia', models.CharField(blank=True, max_length=40)),
                ('ciudad', models.CharField(blank=True, max_length=30)),
                ('estado', models.CharField(blank=True, max_length=19)),
                ('codigoPostal', models.CharField(blank=True, max_length=5)),
                ('idCliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('apellidoPaterno', models.CharField(max_length=30)),
                ('apellidoMaterno', models.CharField(max_length=30)),
                ('linkRegistroRFC', models.URLField(blank=True, null=True)),
                ('linkComprobanteDomicilio', models.URLField(blank=True, null=True)),
                ('calleFact', models.CharField(blank=True, max_length=50)),
                ('numeroExtFact', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('numeroIntFact', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('coloniaFact', models.CharField(blank=True, max_length=40)),
                ('ciudadFact', models.CharField(blank=True, max_length=30)),
                ('estadoFact', models.CharField(blank=True, max_length=19)),
                ('codigoPostalFact', models.CharField(blank=True, max_length=5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CoberturaAP',
            fields=[
                ('idCobertura', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=41)),
                ('sumaAsegurada', models.DecimalField(blank=True, null=True, max_digits=11, decimal_places=11)),
                ('deducible', models.DecimalField(blank=True, null=True, max_digits=11, decimal_places=11)),
                ('primaNeta', models.DecimalField(blank=True, null=True, max_digits=11, decimal_places=11)),
                ('ampliaVip', models.NullBooleanField()),
                ('ampliaUno', models.NullBooleanField()),
                ('limitado', models.NullBooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Comision',
            fields=[
                ('idComision', models.AutoField(primary_key=True, serialize=False)),
                ('cantidadComision', models.DecimalField(max_digits=11, decimal_places=2)),
                ('fechaDeposito', models.DateTimeField(blank=True, null=True)),
                ('agente', models.ForeignKey(to='schema.Agente')),
                ('asignacionComision', models.ForeignKey(null=True, to='schema.AsignacionComision')),
            ],
        ),
        migrations.CreateModel(
            name='Comparativa',
            fields=[
                ('idComparativa', models.AutoField(primary_key=True, serialize=False)),
                ('fechaCreacion', models.DateTimeField(verbose_name='fecha creada', auto_now_add=True)),
                ('fechaConclusion', models.DateTimeField(blank=True, null=True, verbose_name='fecha concluida')),
                ('fechaEnvio', models.DateTimeField(blank=True, null=True, verbose_name='fecha de envio')),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('idContacto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('apellidoPaterno', models.CharField(max_length=30)),
                ('apellidoMaterno', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, null=True, max_length=254)),
                ('telefonoLada', models.CharField(blank=True, max_length=3)),
                ('telefono', models.CharField(blank=True, max_length=7)),
                ('aseguradora', models.ForeignKey(to='schema.Aseguradora')),
            ],
        ),
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('idCotizacion', models.AutoField(primary_key=True, serialize=False)),
                ('costo', models.DecimalField(max_digits=11, decimal_places=2)),
                ('fechaCreacion', models.DateTimeField(verbose_name='fecha creada', auto_now_add=True)),
                ('formaPago', models.IntegerField(default=12, choices=[(12, 'Anual'), (6, 'Semestral'), (3, 'Trimestral')])),
                ('aseguradora', models.ForeignKey(to='schema.Aseguradora')),
                ('comparativa', models.ForeignKey(to='schema.Comparativa')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenServicio',
            fields=[
                ('idServicio', models.AutoField(primary_key=True, serialize=False)),
                ('fechaServicio', models.DateTimeField(verbose_name='fecha de servicio', auto_now_add=True)),
                ('fechaConclusion', models.DateTimeField(blank=True, null=True)),
                ('agente', models.ForeignKey(to='schema.Agente')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('idPago', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.DecimalField(max_digits=11, decimal_places=2)),
                ('fechaPago', models.DateTimeField(verbose_name='fecha de pago', auto_now_add=True)),
                ('numeroPago', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Poliza',
            fields=[
                ('idPoliza', models.AutoField(primary_key=True, serialize=False)),
                ('primaNeta', models.DecimalField(max_digits=11, decimal_places=2)),
                ('fechaEmision', models.DateTimeField(verbose_name='fecha emitida')),
                ('fechaInicio', models.DateTimeField(verbose_name='fecha de inicio')),
                ('fechaFin', models.DateTimeField(verbose_name='fecha de fin')),
                ('endosoBeneficiario', models.CharField(blank=True, max_length=50)),
                ('linkCaratulaPDF', models.URLField()),
                ('comision', models.OneToOneField(to='schema.Comision')),
                ('cotizacion', models.OneToOneField(to='schema.Cotizacion')),
                ('ordenServicio', models.OneToOneField(to='schema.OrdenServicio')),
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
                ('idTipoSeguro', models.CharField(max_length=3, serialize=False, choices=[('AP', 'Automoviles y pickups'), ('C', 'Camiones'), ('R', 'Remolques, cajas secas y adaptaciones en general'), ('G', 'Gastos medicos mayores'), ('V', 'Vida'), ('H', 'Hogares'), ('I', 'Inversion'), ('E', 'Empresas'), ('EC', 'Equipo de contratistas'), ('T', 'Transportes'), ('ESP', 'Especializados')], primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClienteFisico',
            fields=[
                ('cliente_ptr', models.OneToOneField(serialize=False, to='schema.Cliente', parent_link=True, primary_key=True, auto_created=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('schema.cliente',),
        ),
        migrations.CreateModel(
            name='ClienteMoral',
            fields=[
                ('cliente_ptr', models.OneToOneField(serialize=False, to='schema.Cliente', parent_link=True, primary_key=True, auto_created=True)),
                ('razonSocial', models.CharField(null=True, max_length=100)),
                ('linkActaConstitutiva', models.URLField(null=True)),
                ('linkIdRepresentante', models.URLField(null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('schema.cliente',),
        ),
        migrations.CreateModel(
            name='SeguroAP',
            fields=[
                ('tiposeguro_ptr', models.OneToOneField(to='schema.TipoSeguro', parent_link=True, auto_created=True)),
                ('idSeguro', models.AutoField(primary_key=True, serialize=False)),
                ('marca', models.CharField(blank=True, null=True, max_length=30)),
                ('modelo', models.CharField(blank=True, null=True, max_length=30)),
                ('ano', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('pasajeros', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('estadoCirculacion', models.CharField(blank=True, null=True, max_length=19)),
            ],
            bases=('schema.tiposeguro',),
        ),
        migrations.AddField(
            model_name='segurosofertados',
            name='tipoSeguro',
            field=models.ForeignKey(to='schema.TipoSeguro'),
        ),
        migrations.AddField(
            model_name='pago',
            name='poliza',
            field=models.ForeignKey(to='schema.Poliza'),
        ),
        migrations.AddField(
            model_name='ordenservicio',
            name='cliente',
            field=models.ForeignKey(to='schema.Cliente'),
        ),
        migrations.AddField(
            model_name='ordenservicio',
            name='tipoSeguro',
            field=models.ForeignKey(to='schema.TipoSeguro'),
        ),
        migrations.AddField(
            model_name='comparativa',
            name='ordenServicio',
            field=models.OneToOneField(to='schema.OrdenServicio'),
        ),
        migrations.AddField(
            model_name='asignacioncomision',
            name='tipoSeguro',
            field=models.ForeignKey(to='schema.TipoSeguro'),
        ),
        migrations.AddField(
            model_name='aseguradora',
            name='seguros',
            field=models.ManyToManyField(to='schema.TipoSeguro', through='schema.SegurosOfertados'),
        ),
        migrations.AddField(
            model_name='agente',
            name='clientes',
            field=models.ManyToManyField(to='schema.Cliente', through='schema.OrdenServicio'),
        ),
        migrations.AddField(
            model_name='agente',
            name='userAgente',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='segurosofertados',
            unique_together=set([('aseguradora', 'tipoSeguro')]),
        ),
        migrations.AddField(
            model_name='coberturaap',
            name='seguroAP',
            field=models.ForeignKey(to='schema.SeguroAP'),
        ),
    ]
