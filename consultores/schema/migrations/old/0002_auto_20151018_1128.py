# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClienteFisico',
            fields=[
                ('cliente_ptr', models.OneToOneField(primary_key=True, serialize=False, parent_link=True, to='schema.Cliente', auto_created=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('schema.cliente',),
        ),
        migrations.CreateModel(
            name='CoberturasRequeridas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='CoberturasUtilizadas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='DatosNecesitados',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='SegurosOfertados',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='clientefisica',
            name='cliente_ptr',
        ),
        migrations.RemoveField(
            model_name='cobertura',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='comision',
            name='asignacionComision',
        ),
        migrations.RemoveField(
            model_name='comparativa',
            name='fechaConclusion',
        ),
        migrations.RemoveField(
            model_name='comparativa',
            name='fechaCreacion',
        ),
        migrations.RemoveField(
            model_name='comparativa',
            name='fechaEnvio',
        ),
        migrations.RemoveField(
            model_name='comparativa',
            name='tipoSeguro',
        ),
        migrations.RemoveField(
            model_name='dato',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='ordenservicio',
            name='fechaServicio',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='servicio',
        ),
        migrations.AddField(
            model_name='agente',
            name='edad',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='agente',
            name='rfc',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='agente',
            name='sexo',
            field=models.CharField(max_length=1, default=None, choices=[(None, '-'), ('M', 'Mujer'), ('H', 'Hombre'), ('O', 'Otro')]),
        ),
        migrations.AddField(
            model_name='asignacioncomision',
            name='comision',
            field=models.ForeignKey(to='schema.Comision', null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='calleFact',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='ciudadFact',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='codigoPostalFact',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='coloniaFact',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='edad',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='estadoFact',
            field=models.CharField(max_length=19, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='numeroExtFact',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='numeroIntFact',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='rfc',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='sexo',
            field=models.CharField(max_length=1, default=None, choices=[(None, '-'), ('M', 'Mujer'), ('H', 'Hombre'), ('O', 'Otro')]),
        ),
        migrations.AddField(
            model_name='cobertura',
            name='nombreCobertura',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='cobertura',
            name='seguro',
            field=models.ForeignKey(to='schema.TipoSeguro', null=True),
        ),
        migrations.AddField(
            model_name='comision',
            name='agente',
            field=models.ForeignKey(to='schema.Agente', null=True),
        ),
        migrations.AddField(
            model_name='comparativa',
            name='agente',
            field=models.ForeignKey(to='schema.Agente', null=True),
        ),
        migrations.AddField(
            model_name='comparativa',
            name='cliente',
            field=models.ForeignKey(to='schema.Cliente', null=True),
        ),
        migrations.AddField(
            model_name='contacto',
            name='aseguradora',
            field=models.ForeignKey(to='schema.Aseguradora', null=True),
        ),
        migrations.AddField(
            model_name='dato',
            name='nombreDato',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='dato',
            name='tipoDato',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='ordenservicio',
            name='comparativa',
            field=models.ForeignKey(to='schema.Comparativa', null=True),
        ),
        migrations.AddField(
            model_name='ordenservicio',
            name='fechaConclusion',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ordenservicio',
            name='poliza',
            field=models.ForeignKey(to='schema.Poliza', null=True),
        ),
        migrations.AddField(
            model_name='ordenservicio',
            name='tipoSeguro',
            field=models.ForeignKey(to='schema.TipoSeguro', null=True),
        ),
        migrations.AddField(
            model_name='pago',
            name='numeroPago',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pago',
            name='poliza',
            field=models.ForeignKey(to='schema.Poliza', null=True),
        ),
        migrations.AddField(
            model_name='poliza',
            name='agente',
            field=models.ForeignKey(to='schema.Agente', null=True),
        ),
        migrations.AddField(
            model_name='poliza',
            name='aseguradora',
            field=models.ForeignKey(to='schema.Aseguradora', null=True),
        ),
        migrations.AddField(
            model_name='poliza',
            name='cliente',
            field=models.ForeignKey(to='schema.Cliente', null=True),
        ),
        migrations.AlterField(
            model_name='agente',
            name='apellidoMaterno',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='agente',
            name='apellidoPaterno',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='agente',
            name='banco',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='agente',
            name='calle',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='agente',
            name='ciudad',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='agente',
            name='claveAgente',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='agente',
            name='codigoPostal',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='agente',
            name='colonia',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='agente',
            name='contrasena',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='agente',
            name='cuentaBancaria',
            field=models.CharField(max_length=34, null=True),
        ),
        migrations.AlterField(
            model_name='agente',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='agente',
            name='estado',
            field=models.CharField(blank=True, max_length=19, null=True),
        ),
        migrations.AlterField(
            model_name='agente',
            name='nombre',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='agente',
            name='numeroExt',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='agente',
            name='numeroInt',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='agente',
            name='telefono',
            field=models.CharField(max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='agente',
            name='telefonoLada',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='agente',
            name='usuario',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='aseguradora',
            name='calle',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='aseguradora',
            name='ciudad',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='aseguradora',
            name='codigoPostal',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='aseguradora',
            name='colonia',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='aseguradora',
            name='estado',
            field=models.CharField(blank=True, max_length=19, null=True),
        ),
        migrations.AlterField(
            model_name='aseguradora',
            name='nombre',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='aseguradora',
            name='numeroExt',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aseguradora',
            name='numeroInt',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aseguradora',
            name='sitioWeb',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aseguradora',
            name='telefono',
            field=models.CharField(max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='aseguradora',
            name='telefonoLada',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='asignacioncomision',
            name='aseguradora',
            field=models.ForeignKey(to='schema.Aseguradora', null=True),
        ),
        migrations.AlterField(
            model_name='asignacioncomision',
            name='fechaAsignacion',
            field=models.DateTimeField(verbose_name='fecha de asignacion'),
        ),
        migrations.AlterField(
            model_name='asignacioncomision',
            name='porcentaje',
            field=models.DecimalField(decimal_places=2, null=True, max_digits=4),
        ),
        migrations.AlterField(
            model_name='asignacioncomision',
            name='tipoSeguro',
            field=models.ForeignKey(to='schema.TipoSeguro', null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='apellidoMaterno',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='apellidoPaterno',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='calle',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='ciudad',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='codigoPostal',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='colonia',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='contrasena',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='estado',
            field=models.CharField(blank=True, max_length=19, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='linkComprobanteDomicilio',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='linkRegistroRFC',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='numeroExt',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='numeroInt',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefonoLada',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='usuario',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='clientemoral',
            name='linkActaConstitutiva',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='clientemoral',
            name='linkIdRepresentante',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='clientemoral',
            name='razonSocial',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cobertura',
            name='descripcion',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='cobertura',
            name='porcentajeCobertura',
            field=models.DecimalField(decimal_places=2, null=True, max_digits=4),
        ),
        migrations.AlterField(
            model_name='comision',
            name='cantidadComision',
            field=models.DecimalField(decimal_places=2, null=True, max_digits=11),
        ),
        migrations.AlterField(
            model_name='comparativa',
            name='numeroCotizaciones',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='apellidoMaterno',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='apellidoPaterno',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='nombre',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='telefono',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='telefonoLada',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='aseguradora',
            field=models.ForeignKey(to='schema.Aseguradora', null=True),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='comparativa',
            field=models.ForeignKey(to='schema.Comparativa', null=True),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='costo',
            field=models.DecimalField(decimal_places=2, null=True, max_digits=11),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='fechaCreacion',
            field=models.DateTimeField(verbose_name='fecha creada', null=True),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='formaPago',
            field=models.IntegerField(null=True, default=12, choices=[(12, 'Anual'), (6, 'Semestral'), (3, 'Trimestral')]),
        ),
        migrations.AlterField(
            model_name='dato',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ordenservicio',
            name='agente',
            field=models.ForeignKey(to='schema.Agente', null=True),
        ),
        migrations.AlterField(
            model_name='ordenservicio',
            name='cliente',
            field=models.ForeignKey(to='schema.Cliente', null=True),
        ),
        migrations.AlterField(
            model_name='pago',
            name='cantidad',
            field=models.DecimalField(decimal_places=2, null=True, max_digits=11),
        ),
        migrations.AlterField(
            model_name='pago',
            name='fechaPago',
            field=models.DateTimeField(verbose_name='fecha de pago', null=True),
        ),
        migrations.AlterField(
            model_name='poliza',
            name='comision',
            field=models.ForeignKey(to='schema.Comision', null=True),
        ),
        migrations.AlterField(
            model_name='poliza',
            name='endosoBeneficiario',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='poliza',
            name='fechaEmision',
            field=models.DateTimeField(verbose_name='fecha emitida', null=True),
        ),
        migrations.AlterField(
            model_name='poliza',
            name='fechaFin',
            field=models.DateTimeField(verbose_name='fecha de fin', null=True),
        ),
        migrations.AlterField(
            model_name='poliza',
            name='fechaInicio',
            field=models.DateTimeField(verbose_name='fecha de inicio', null=True),
        ),
        migrations.AlterField(
            model_name='poliza',
            name='linkCaratulaPDF',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='poliza',
            name='primaNeta',
            field=models.DecimalField(decimal_places=2, null=True, max_digits=11),
        ),
        migrations.AlterField(
            model_name='tiposeguro',
            name='nombre',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='ClienteFisica',
        ),
        migrations.AddField(
            model_name='segurosofertados',
            name='aseguradora',
            field=models.ForeignKey(to='schema.Aseguradora'),
        ),
        migrations.AddField(
            model_name='segurosofertados',
            name='seguro',
            field=models.ForeignKey(to='schema.TipoSeguro'),
        ),
        migrations.AddField(
            model_name='datosnecesitados',
            name='dato',
            field=models.ForeignKey(to='schema.Dato', null=True),
        ),
        migrations.AddField(
            model_name='datosnecesitados',
            name='seguro',
            field=models.ForeignKey(to='schema.TipoSeguro', null=True),
        ),
        migrations.AddField(
            model_name='coberturasutilizadas',
            name='cobertura',
            field=models.ForeignKey(to='schema.Cobertura', null=True),
        ),
        migrations.AddField(
            model_name='coberturasutilizadas',
            name='poliza',
            field=models.ForeignKey(to='schema.Poliza', null=True),
        ),
        migrations.AddField(
            model_name='coberturasrequeridas',
            name='cobertura',
            field=models.ForeignKey(to='schema.Cobertura', null=True),
        ),
        migrations.AddField(
            model_name='coberturasrequeridas',
            name='comparativa',
            field=models.ForeignKey(to='schema.Comparativa', null=True),
        ),
    ]
