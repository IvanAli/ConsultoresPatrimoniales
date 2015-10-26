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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('email', models.EmailField(null=True, max_length=254)),
                ('edad', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('sexo', models.CharField(default=None, choices=[(None, '-'), ('M', 'Mujer'), ('H', 'Hombre'), ('O', 'Otro')], max_length=1, blank=True)),
                ('rfc', models.CharField(max_length=13, blank=True, null=True)),
                ('telefonoLada', models.CharField(null=True, max_length=3)),
                ('telefono', models.CharField(null=True, max_length=7)),
                ('calle', models.CharField(max_length=50, blank=True, null=True)),
                ('numeroExt', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('numeroInt', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('colonia', models.CharField(max_length=40, blank=True, null=True)),
                ('ciudad', models.CharField(max_length=30, blank=True, null=True)),
                ('estado', models.CharField(max_length=19, blank=True, null=True)),
                ('codigoPostal', models.CharField(max_length=5, blank=True, null=True)),
                ('claveAgente', models.IntegerField(null=True, blank=True)),
                ('cuentaBancaria', models.CharField(null=True, max_length=34)),
                ('banco', models.CharField(null=True, max_length=30)),
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
                ('sitioWeb', models.URLField(blank=True, null=True)),
                ('telefonoLada', models.CharField(null=True, max_length=3)),
                ('telefono', models.CharField(null=True, max_length=7)),
                ('calle', models.CharField(max_length=50, blank=True, null=True)),
                ('numeroExt', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('numeroInt', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('colonia', models.CharField(max_length=40, blank=True, null=True)),
                ('ciudad', models.CharField(max_length=30, blank=True, null=True)),
                ('estado', models.CharField(max_length=19, blank=True, null=True)),
                ('codigoPostal', models.CharField(max_length=5, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AsignacionComision',
            fields=[
                ('idAsignacion', models.AutoField(primary_key=True, serialize=False)),
                ('fechaAsignacion', models.DateTimeField(verbose_name='fecha de asignacion')),
                ('porcentaje', models.DecimalField(max_digits=4, null=True, decimal_places=2)),
                ('aseguradora', models.ForeignKey(to='schema.Aseguradora', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('email', models.EmailField(null=True, max_length=254)),
                ('edad', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('sexo', models.CharField(default=None, choices=[(None, '-'), ('M', 'Mujer'), ('H', 'Hombre'), ('O', 'Otro')], max_length=1, blank=True)),
                ('rfc', models.CharField(max_length=13, blank=True, null=True)),
                ('telefonoLada', models.CharField(null=True, max_length=3)),
                ('telefono', models.CharField(null=True, max_length=7)),
                ('calle', models.CharField(max_length=50, blank=True, null=True)),
                ('numeroExt', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('numeroInt', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('colonia', models.CharField(max_length=40, blank=True, null=True)),
                ('ciudad', models.CharField(max_length=30, blank=True, null=True)),
                ('estado', models.CharField(max_length=19, blank=True, null=True)),
                ('codigoPostal', models.CharField(max_length=5, blank=True, null=True)),
                ('nombre', models.CharField(null=True, max_length=40)),
                ('apellidoPaterno', models.CharField(max_length=30, blank=True, null=True)),
                ('apellidoMaterno', models.CharField(max_length=30, blank=True, null=True)),
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
            ],
        ),
        migrations.CreateModel(
            name='Comision',
            fields=[
                ('idComision', models.AutoField(primary_key=True, serialize=False)),
                ('cantidadComision', models.DecimalField(max_digits=11, null=True, decimal_places=2)),
                ('fechaDeposito', models.DateTimeField(null=True)),
                ('agente', models.ForeignKey(to='schema.Agente', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comparativa',
            fields=[
                ('idComparativa', models.AutoField(primary_key=True, serialize=False)),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True, verbose_name='fecha creada', null=True)),
                ('fechaConclusion', models.DateTimeField(verbose_name='fecha concluida', null=True, blank=True)),
                ('fechaEnvio', models.DateTimeField(verbose_name='fecha de envio', null=True, blank=True)),
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
                ('telefonoLada', models.CharField(max_length=3, blank=True, null=True)),
                ('telefono', models.CharField(max_length=7, blank=True, null=True)),
                ('aseguradora', models.ForeignKey(to='schema.Aseguradora', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('idCotizacion', models.AutoField(primary_key=True, serialize=False)),
                ('costo', models.DecimalField(max_digits=11, null=True, decimal_places=2)),
                ('fechaCreacion', models.DateTimeField(verbose_name='fecha creada', null=True)),
                ('formaPago', models.IntegerField(default=12, choices=[(12, 'Anual'), (6, 'Semestral'), (3, 'Trimestral')], null=True)),
                ('aseguradora', models.ForeignKey(to='schema.Aseguradora', null=True)),
                ('comparativa', models.ForeignKey(to='schema.Comparativa', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DatoCobertura',
            fields=[
                ('llave', models.CharField(primary_key=True, serialize=False, max_length=40)),
                ('valor', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='DatoTipoSeguro',
            fields=[
                ('llave', models.CharField(primary_key=True, serialize=False, max_length=40)),
                ('valor', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='OrdenServicio',
            fields=[
                ('idServicio', models.AutoField(primary_key=True, serialize=False)),
                ('fechaServicio', models.DateTimeField(auto_now_add=True, verbose_name='fecha de servicio')),
                ('fechaConclusion', models.DateTimeField(null=True, blank=True)),
                ('agente', models.ForeignKey(to='schema.Agente', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('idPago', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.DecimalField(max_digits=11, null=True, decimal_places=2)),
                ('fechaPago', models.DateTimeField(verbose_name='fecha de pago', null=True)),
                ('numeroPago', models.PositiveSmallIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Poliza',
            fields=[
                ('idPoliza', models.AutoField(primary_key=True, serialize=False)),
                ('primaNeta', models.DecimalField(max_digits=11, null=True, decimal_places=2)),
                ('fechaEmision', models.DateTimeField(verbose_name='fecha emitida', null=True)),
                ('fechaInicio', models.DateTimeField(verbose_name='fecha de inicio', null=True)),
                ('fechaFin', models.DateTimeField(verbose_name='fecha de fin', null=True)),
                ('endosoBeneficiario', models.CharField(null=True, max_length=50)),
                ('linkCaratulaPDF', models.URLField(null=True)),
                ('comision', models.OneToOneField(to='schema.Comision', null=True)),
                ('cotizacion', models.OneToOneField(to='schema.Cotizacion', null=True)),
                ('ordenServicio', models.OneToOneField(to='schema.OrdenServicio', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoSeguro',
            fields=[
                ('idTipoSeguro', models.CharField(choices=[('AP', 'Automoviles y pickups'), ('C', 'Camiones'), ('R', 'Remolques, cajas secas y adaptaciones en general'), ('G', 'Gastos medicos mayores'), ('V', 'Vida'), ('H', 'Hogares'), ('I', 'Inversion'), ('E', 'Empresas'), ('EC', 'Equipo de contratistas'), ('T', 'Transportes'), ('ESP', 'Especializados')], primary_key=True, serialize=False, max_length=3)),
                ('aseguradora', models.ForeignKey(to='schema.Aseguradora', null=True)),
                ('datos', models.ManyToManyField(to='schema.DatoTipoSeguro')),
            ],
        ),
        migrations.CreateModel(
            name='ClienteFisico',
            fields=[
                ('cliente_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='schema.Cliente', primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('schema.cliente',),
        ),
        migrations.CreateModel(
            name='ClienteMoral',
            fields=[
                ('cliente_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='schema.Cliente', primary_key=True, serialize=False)),
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
            model_name='pago',
            name='poliza',
            field=models.ForeignKey(to='schema.Poliza', null=True),
        ),
        migrations.AddField(
            model_name='ordenservicio',
            name='cliente',
            field=models.ForeignKey(to='schema.Cliente', null=True),
        ),
        migrations.AddField(
            model_name='ordenservicio',
            name='tipoSeguro',
            field=models.ForeignKey(to='schema.TipoSeguro', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='datotiposeguro',
            unique_together=set([('llave', 'valor')]),
        ),
        migrations.AlterUniqueTogether(
            name='datocobertura',
            unique_together=set([('llave', 'valor')]),
        ),
        migrations.AddField(
            model_name='comparativa',
            name='ordenServicio',
            field=models.OneToOneField(to='schema.OrdenServicio', null=True),
        ),
        migrations.AddField(
            model_name='cobertura',
            name='datos',
            field=models.ManyToManyField(to='schema.DatoCobertura'),
        ),
        migrations.AddField(
            model_name='cobertura',
            name='tipoSeguro',
            field=models.ForeignKey(to='schema.TipoSeguro', null=True),
        ),
        migrations.AddField(
            model_name='asignacioncomision',
            name='comision',
            field=models.ForeignKey(to='schema.Comision', null=True),
        ),
        migrations.AddField(
            model_name='asignacioncomision',
            name='tipoSeguro',
            field=models.ForeignKey(to='schema.TipoSeguro', null=True),
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
            name='tiposeguro',
            unique_together=set([('idTipoSeguro', 'aseguradora')]),
        ),
    ]
