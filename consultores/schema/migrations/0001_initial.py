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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('email', models.EmailField(null=True, max_length=254, blank=True)),
                ('edad', models.PositiveSmallIntegerField(null=True)),
                ('sexo', models.CharField(default='M', max_length=1, choices=[(None, '-'), ('M', 'Mujer'), ('H', 'Hombre'), ('O', 'Otro')])),
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
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('email', models.EmailField(null=True, max_length=254, blank=True)),
                ('edad', models.PositiveSmallIntegerField(null=True)),
                ('sexo', models.CharField(default='M', max_length=1, choices=[(None, '-'), ('M', 'Mujer'), ('H', 'Hombre'), ('O', 'Otro')])),
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
            ],
        ),
        migrations.CreateModel(
            name='DatoCobertura',
            fields=[
                ('llave', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('valor', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='DatoTipoSeguro',
            fields=[
                ('llave', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('valor', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='TipoSeguro',
            fields=[
                ('idTipoSeguro', models.CharField(max_length=3, choices=[('AP', 'Automoviles y pickups'), ('C', 'Camiones'), ('R', 'Remolques, cajas secas y adaptaciones en general'), ('G', 'Gastos medicos mayores'), ('V', 'Vida'), ('H', 'Hogares'), ('I', 'Inversion'), ('E', 'Empresas'), ('EC', 'Equipo de contratistas'), ('T', 'Transportes'), ('ESP', 'Especializados')], primary_key=True, serialize=False)),
                ('aseguradora', models.ForeignKey(to='schema.Aseguradora')),
                ('datos', models.ManyToManyField(to='schema.DatoTipoSeguro')),
            ],
        ),
        migrations.CreateModel(
            name='ClienteFisico',
            fields=[
                ('cliente_ptr', models.OneToOneField(primary_key=True, to='schema.Cliente', serialize=False, parent_link=True, auto_created=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('schema.cliente',),
        ),
        migrations.CreateModel(
            name='ClienteMoral',
            fields=[
                ('cliente_ptr', models.OneToOneField(primary_key=True, to='schema.Cliente', serialize=False, parent_link=True, auto_created=True)),
                ('razonSocial', models.CharField(null=True, max_length=100)),
                ('linkActaConstitutiva', models.URLField(null=True)),
                ('linkIdRepresentante', models.URLField(null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('schema.cliente',),
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
            model_name='cobertura',
            name='datos',
            field=models.ManyToManyField(to='schema.DatoCobertura'),
        ),
        migrations.AddField(
            model_name='cobertura',
            name='tipoSeguro',
            field=models.ForeignKey(to='schema.TipoSeguro'),
        ),
        migrations.AlterUniqueTogether(
            name='tiposeguro',
            unique_together=set([('idTipoSeguro', 'aseguradora')]),
        ),
    ]
