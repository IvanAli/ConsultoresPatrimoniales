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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('email', models.EmailField(null=True, blank=True, max_length=254)),
                ('edad', models.PositiveSmallIntegerField(null=True)),
                ('sexo', models.CharField(default='M', choices=[(None, '-'), ('M', 'Mujer'), ('H', 'Hombre'), ('O', 'Otro')], max_length=1)),
                ('rfc', models.CharField(null=True, max_length=13)),
                ('telefonoLada', models.CharField(null=True, max_length=3)),
                ('telefono', models.CharField(null=True, max_length=7)),
                ('calle', models.CharField(null=True, blank=True, max_length=50)),
                ('numeroExt', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('numeroInt', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('colonia', models.CharField(null=True, blank=True, max_length=40)),
                ('ciudad', models.CharField(null=True, blank=True, max_length=30)),
                ('estado', models.CharField(null=True, blank=True, max_length=19)),
                ('codigoPostal', models.CharField(null=True, blank=True, max_length=5)),
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
                ('idAseguradora', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(null=True, max_length=50)),
                ('sitioWeb', models.URLField(null=True, blank=True)),
                ('telefonoLada', models.CharField(null=True, max_length=3)),
                ('telefono', models.CharField(null=True, max_length=7)),
                ('calle', models.CharField(null=True, blank=True, max_length=50)),
                ('numeroExt', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('numeroInt', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('colonia', models.CharField(null=True, blank=True, max_length=40)),
                ('ciudad', models.CharField(null=True, blank=True, max_length=30)),
                ('estado', models.CharField(null=True, blank=True, max_length=19)),
                ('codigoPostal', models.CharField(null=True, blank=True, max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('email', models.EmailField(null=True, blank=True, max_length=254)),
                ('edad', models.PositiveSmallIntegerField(null=True)),
                ('sexo', models.CharField(default='M', choices=[(None, '-'), ('M', 'Mujer'), ('H', 'Hombre'), ('O', 'Otro')], max_length=1)),
                ('rfc', models.CharField(null=True, max_length=13)),
                ('telefonoLada', models.CharField(null=True, max_length=3)),
                ('telefono', models.CharField(null=True, max_length=7)),
                ('calle', models.CharField(null=True, blank=True, max_length=50)),
                ('numeroExt', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('numeroInt', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('colonia', models.CharField(null=True, blank=True, max_length=40)),
                ('ciudad', models.CharField(null=True, blank=True, max_length=30)),
                ('estado', models.CharField(null=True, blank=True, max_length=19)),
                ('codigoPostal', models.CharField(null=True, blank=True, max_length=5)),
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
                ('idCobertura', models.AutoField(serialize=False, primary_key=True)),
                ('nombreCobertura', models.CharField(null=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoSeguro',
            fields=[
                ('idTipoSeguro', models.CharField(serialize=False, primary_key=True, choices=[('AP', 'Automoviles y pickups'), ('C', 'Camiones'), ('R', 'Remolques, cajas secas y adaptaciones en general'), ('G', 'Gastos medicos mayores'), ('V', 'Vida'), ('H', 'Hogares'), ('I', 'Inversion'), ('E', 'Empresas'), ('EC', 'Equipo de contratistas'), ('T', 'Transportes'), ('ESP', 'Especializados')], max_length=3)),
                ('aseguradora', models.ForeignKey(to='schema.Aseguradora')),
            ],
        ),
        migrations.CreateModel(
            name='ClienteFisico',
            fields=[
                ('cliente_ptr', models.OneToOneField(serialize=False, to='schema.Cliente', primary_key=True, auto_created=True, parent_link=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('schema.cliente',),
        ),
        migrations.CreateModel(
            name='ClienteMoral',
            fields=[
                ('cliente_ptr', models.OneToOneField(serialize=False, to='schema.Cliente', primary_key=True, auto_created=True, parent_link=True)),
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
            model_name='cobertura',
            name='tipoSeguro',
            field=models.ForeignKey(to='schema.TipoSeguro'),
        ),
        migrations.AlterUniqueTogether(
            name='tiposeguro',
            unique_together=set([('idTipoSeguro', 'aseguradora')]),
        ),
    ]
