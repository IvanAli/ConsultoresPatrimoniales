from django.db import models
from django.db.models import OneToOneField
from django.contrib.auth.models import User, Group

"""
 REVISAR IMPLEMENTACION DE URL PARA CADA CLASE
    #def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse()

http://stackoverflow.com/questions/12567151/how-to-add-column-in-manytomany-table-django
"""

SEGUROS_OPCIONES = (
    ('AP', 'Automóviles y pickups'),
    ('C', 'Camiones'),
    ('R', 'Remolques, cajas secas y adaptaciones en general'),
    ('G', 'Gastos médicos mayores'),
    ('V', 'Vida'),
    ('H', 'Hogares'),
    ('I', 'Inversión'),
    ('E', 'Empresas'),
    ('EC', 'Equipo de contratistas'),
    ('T', 'Transportes'),
    ('ESP', 'Especializados'),
)

# Create your models here.
class Persona(models.Model):
    email = models.EmailField(max_length=254, verbose_name='Email')
    edad = models.PositiveSmallIntegerField(null=True, verbose_name='Edad')
    SEXO_OPCIONES = (
        ('M', 'Mujer'),
        ('H', 'Hombre'),
    )
    sexo = models.CharField(max_length=1, choices=SEXO_OPCIONES, verbose_name='Sexo')
    rfc = models.CharField(max_length=13, blank=True, verbose_name='R.F.C.')
    telefonoLada = models.PositiveSmallIntegerField(null=True, verbose_name='Lada')
    telefono = models.PositiveIntegerField(null=True, verbose_name='Teléfono')
    calle = models.CharField(max_length=50, blank=True, verbose_name='Calle')
    numeroExt = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Número Ext.')
    numeroInt = models.CharField(max_length=6,blank=True, null=True, verbose_name='Número Int.')
    colonia = models.CharField(max_length=40, blank=True, verbose_name='Colonia')
    ciudad = models.CharField(max_length=30, blank=True, verbose_name='Ciudad')
    estado = models.CharField(max_length=19, blank=True, verbose_name='Estado')
    codigoPostal = models.PositiveIntegerField(blank=True, null=True, verbose_name='C.P.')
    class Meta:
        abstract = True
    def __str__(self):
        return "Persona"

class Cliente(Persona):
    idCliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, verbose_name='Nombre')
    apellidoPaterno = models.CharField(max_length=30, verbose_name='Apellido Paterno')
    apellidoMaterno = models.CharField(max_length=30, verbose_name='Apellido Materno')
    linkRegistroRFC = models.URLField(blank=True, null=True, verbose_name='Registro R.F.C.')
    linkComprobanteDomicilio = models.FileField(null=True, verbose_name='Comprobante de Domicilio')
    calleFact = models.CharField(max_length=50, blank=True,null=True, verbose_name='Calle')
    numeroExtFact = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Número Ext.')
    numeroIntFact = models.CharField(max_length=6, blank=True, null=True, verbose_name='Número Int.')
    coloniaFact = models.CharField(max_length=40, blank=True, null=True, verbose_name='Colonia')
    ciudadFact = models.CharField(max_length=30, blank=True, null=True, verbose_name='Ciudad')
    estadoFact = models.CharField(max_length=19, blank=True, null=True, verbose_name='Estado')
    codigoPostalFact = models.PositiveIntegerField(blank=True, null=True, verbose_name='C.P.')
    def __str__(self):
        return "Cliente fisico: " + self.nombre + " " +self.apellidoPaterno + " " + self.apellidoMaterno

#Creo que seria mejor agregar como campos dentro de Cliente
class ClienteFisico(Cliente):
    def __str__(self):
        return "Cliente fisico"

#Creo que seria mejor agregar como campos dentro de Cliente
class ClienteMoral(Cliente):
    razonSocial = models.CharField(max_length=100, null=True, verbose_name='Razón Social')
    linkActaConstitutiva = models.URLField(null=True, verbose_name='Acta Constitutiva')
    linkIdRepresentante = models.URLField(null=True, verbose_name='ID del Representante')
    def __str__(self):
        return "Cliente moral"

class Agente(Persona):
    userAgente = OneToOneField(User)
    claveAgente = models.IntegerField(blank=True, null=True, verbose_name='Clave de Agente')
    cuentaBancaria = models.CharField(max_length=34, blank=True, verbose_name='Cuenta Bancaria')
    banco = models.CharField(max_length=30, blank=True, verbose_name='Banco')
    clientes = models.ManyToManyField(Cliente, through='ClienteAgente')

    def save(self, *args, **kwargs):
        try:
            groupAgente = Group.objects.get(name='agente')
            self.userAgente.groups.add(groupAgente)
        except Group.DoesNotExist:
            groupAgente = Group.objects.create(name='agente')
            self.userAgente.groups.add(groupAgente)
        self.userAgente.groups.add(groupAgente)
        super(Agente, self).save(*args, **kwargs)

    def __str__(self):
        return "Agente: " + self.userAgente.username

class ClienteAgente(models.Model):
    cliente = models.ForeignKey(Cliente)
    agente = models.ForeignKey(Agente)
    fecha = models.DateField(auto_now_add=True, verbose_name='Fecha de Registro')

class Administrador(Persona):
    userAdmin = OneToOneField(User)

    def save(self, *args, **kwargs):
        try:
            groupAdmin = Group.objects.get(name='admin')
            self.userAdmin.groups.add(groupAdmin)
        except Group.DoesNotExist:
            groupAdmin = Group.objects.create(name='admin')
            self.userAdmin.groups.add(groupAdmin)
        self.userAdmin.groups.add(groupAdmin)
        super(Administrador, self).save(*args, **kwargs)

    def __str__(self):
        return "Administrador: " + self.userAdmin.username

class TipoSeguro(models.Model):
    # tipo = models.CharField(max_length=3, choices=SEGUROS_OPCIONES, null=True)
    idTipoSeguro = models.AutoField(primary_key=True)
    nombre = models.ForeignKey('Seguro', null=True)
    def attrs(self):
        print("Not implemented")

class Aseguradora(models.Model):
    idAseguradora = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    sitioWeb = models.URLField(blank=True, null=True, verbose_name='Sitio Web')
    telefonoLada = models.CharField(max_length=3, blank=True, verbose_name='Lada')
    telefono = models.CharField(max_length=7, blank=True, verbose_name='Teléfono')
    calle = models.CharField(max_length=50, blank=True, verbose_name='Calle')
    numeroExt = models.PositiveSmallIntegerField(blank=True, verbose_name='Número Ext.')
    numeroInt = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Número Int.')
    colonia = models.CharField(max_length=40, blank=True, verbose_name='Colonia')
    ciudad = models.CharField(max_length=30, blank=True, verbose_name='Ciudad')
    estado = models.CharField(max_length=19, blank=True, verbose_name='Estado')
    codigoPostal = models.CharField(max_length=5, blank=True, verbose_name='C.P.')
    seguros = models.ManyToManyField(TipoSeguro)

    def __str__(self):
        return self.nombre

class Comparativa(models.Model):
    idComparativa = models.AutoField(primary_key=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    fechaConclusion = models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Conclusión')
    fechaEnvioCliente = models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Envío a Cliente')
    fechaEnvioTramite = models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Envío a Trámites')
    tipoSeguro = models.ForeignKey('TipoSeguro')
    coberturas = models.ManyToManyField('Cobertura')
    cotizacionElegida = models.OneToOneField('Cotizacion', related_name='comparativaPreferida', null=True)

class Cotizacion(models.Model):
    idCotizacion = models.AutoField(primary_key=True)
    costo = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Costo')
    fechaCreacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    FORMA_PAGO_OPCIONES = (
        (1, 'Anual'),
        (2, 'Semestral'),
        (4, 'Trimestral'),
        (12, 'Mensual'),
    )
    formaPago = models.IntegerField(choices=FORMA_PAGO_OPCIONES, default=12, verbose_name='Forma de Pago')
    comparativa = models.ForeignKey('Comparativa', null=True)
    aseguradora = models.ForeignKey('Aseguradora')
    archivo = models.FileField(null=True, blank=True, verbose_name='Archivo')
    elegida = models.BooleanField(default=False, verbose_name='Elegida')
    def __str__(self):
        return "Cotizacion: " + self.idCotizacion + " de comparativa: " + self.comparativa

class AreaTramites(models.Model):
    idAreaTramites = models.AutoField(primary_key=True)
    encargado = models.CharField(max_length=60, null=True, verbose_name='Nombre del Encargado')
    email = models.EmailField(null=True, verbose_name='Email')

class Poliza(models.Model):
    idPoliza = models.AutoField(primary_key=True)
    noPoliza = models.CharField(max_length=20, null=True, verbose_name='Número de póliza')
    primaNeta = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Prima Neta')
    fechaEmision = models.DateTimeField(verbose_name='Fecha de Emisión')
    fechaInicio = models.DateTimeField(verbose_name='Fecha de Inicio')
    fechaFin = models.DateTimeField(null=True, verbose_name='Fecha de Fin')
    endosoBeneficiario = models.CharField(max_length=100, blank=True, verbose_name='Nombre del Beneficiario Endosado')
    caratulaPDF = models.FileField(null=True, verbose_name='Carátula de Póliza')
    comision = models.OneToOneField('Comision', null=True)
    cotizacion = models.OneToOneField('Cotizacion', null=True)
    ordenServicio = models.OneToOneField('OrdenServicio', null=True)

class Pago(models.Model):
    idPago = models.AutoField(primary_key=True)
    cantidad = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Cantidad')
    fechaPago = models.DateTimeField(verbose_name='Fecha de Pago')
    numeroPago = models.PositiveSmallIntegerField(verbose_name='Número de Pago')
    comprobante = models.FileField(null=True, verbose_name='Comprobante')
    poliza = models.ForeignKey('Poliza')
    def __str__(self):
        return "Pago " + str(self.numeroPago)

class Comision(models.Model):
    idComision = models.AutoField(primary_key=True)
    cantidadComision = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Comisión Total')
    fechaDeposito = models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Depósito')
    asignacionComision = models.ForeignKey('AsignacionComision', null=True)
    # agente = models.ForeignKey('Agente')
    def __str__(self):
        return "Comisión " + str(self.idComision) + " de " + self.agente

class AsignacionComision(models.Model):
    idAsignacion = models.AutoField(primary_key=True)
    fechaAsignacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Asignación')
    porcentaje = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Porcentaje')
    seguro = models.ForeignKey('Seguro', null=True)
    aseguradora = models.ForeignKey('Aseguradora')
    def __str__(self):
        return "Asignacion de Comisión: " + self.idAsignacion + " Tipo de Seguro: " + self.tipoSeguro + " Aseguradora: " + self.aseguradora

class Contacto(models.Model):
    idContacto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, verbose_name='Nombre')
    apellidoPaterno = models.CharField(max_length=30, verbose_name='apellido Paterno')
    apellidoMaterno = models.CharField(max_length=30, verbose_name='Apellido Materno')
    email = models.EmailField(max_length=254, blank=True, null=True, verbose_name='Email')
    telefonoLada = models.CharField(max_length=3, blank=True, verbose_name='Lada')
    telefono = models.CharField(max_length=7, blank=True, verbose_name='Teléfono')
    aseguradora = models.ForeignKey('Aseguradora')
    def __str__(self):
        return "Contacto: " + self.idContacto + " Aseguradora: " + self.aseguradora


class OrdenServicio(models.Model):
    idServicio = models.AutoField(primary_key=True)
    fechaServicio = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Servicio')
    fechaConclusion = models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Conclusión')
    agente = models.ForeignKey('Agente', null=True)
    cliente = models.ForeignKey('Cliente')
    comparativa = models.OneToOneField(Comparativa, related_name="ordenServicio", null=True)
    # poliza = models.OneToOneField(Poliza, null=True)
    def __str__ (self):
        return "Orden de Servicio: " + str(self.idServicio)

class Cobertura(models.Model):
    idCobertura = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    seguro = models.ForeignKey('Seguro', null=True)
    def __str__(self):
        return self.nombre

class CoberturaUtilizada(models.Model):
    idCoberturaUtilizada = models.AutoField(primary_key=True)
    idCobertura = models.ForeignKey(Cobertura)
    sumaAsegurada = models.CharField(max_length=30, verbose_name='Suma Asegurada')
    deducible = models.DecimalField(max_digits=4, decimal_places=2, blank=True, verbose_name='Deducible')
    cotizacion = models.ForeignKey('Cotizacion', null=True)

class Seguro(models.Model):
    idSeguro = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=80, verbose_name='Nombre')

class SeguroAP(models.Model):
    tipoSeguro = OneToOneField(TipoSeguro, related_name='seguroAP', null=True)
    idSeguro = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=30, null=True, verbose_name='Marca')
    modelo = models.CharField(max_length=30, blank=True, null=True, verbose_name='Modelo')
    tipoPlan = models.CharField(max_length=50, blank=True, default="", verbose_name='Tipo de Plan')
    ano = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Año')
    descripcion = models.TextField(blank=True, null=True, verbose_name='Descripción')
    pasajeros = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Cantidad de Pasajeros')
    estadoCirculacion = models.CharField(max_length=19, blank=True, null=True, verbose_name='Estado de Circulación')
    version = models.CharField(max_length=10, blank=True, verbose_name='Versión')
    TRANSMISIONES_OPCIONES = (
        ("M", "Manual"),
        ("A", "Automática"),
    )
    transmision = models.CharField(max_length=1, choices=TRANSMISIONES_OPCIONES, null=True, blank=True, verbose_name='Transmisión')

    def attrs(self):
        print("Implemented")
        for attr, value in self.__dict__.items():
            yield attr, value


class SeguroC(models.Model):
    tipoSeguro = OneToOneField(TipoSeguro, related_name='seguroC', null=True)
    idSeguro = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=30, null=True, blank=True, verbose_name='Marca')
    modelo = models.CharField(max_length=30, blank=True, null=True, verbose_name='Modelo')
    ano = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Año')
    descripcion = models.TextField(blank=True, null=True, verbose_name='Descripción')
    pasajeros = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Cantidad de Pasajeros')
    unidad = models.PositiveSmallIntegerField(verbose_name='Número de Unidad')
    TRANSMISIONES_OPCIONES = (
        ("M", "Manual"),
        ("A", "Automática"),
    )
    transmision = models.CharField(max_length=1, choices=TRANSMISIONES_OPCIONES, verbose_name='Transmisión')

    def attrs(self):
        for attr, value in self.__dict__.items():
            yield attr, value

class SeguroR(models.Model):
    tipoSeguro = OneToOneField(TipoSeguro, related_name='seguroR', null=True)

    idSeguro = models.AutoField(primary_key=True)
    capacidad = models.CharField(max_length=15, verbose_name='Capacidad')
    ejes = models.PositiveSmallIntegerField(verbose_name='Cantidad de Ejes')
    descripcion = models.TextField(blank=True, null=True, verbose_name='Descripción')

    def attrs(self):
        for attr, value in self.__dict__.items():
            yield attr, value

class SeguroG(models.Model):
    tipoSeguro = OneToOneField(TipoSeguro, related_name='seguroG', null=True)

    idSeguro = models.AutoField(primary_key=True)
    nombreAsegurado = models.CharField(max_length=80, verbose_name='Nombre de Asegurado')
    coaseguro = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Coaseguro')
    topeCoaseguro = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Tope del Coaseguro')

    def attrs(self):
        for attr, value in self.__dict__.items():
            yield attr, value

class SeguroV(models.Model):
    tipoSeguro = OneToOneField(TipoSeguro, related_name='seguroV', null=True)

    idSeguro = models.AutoField(primary_key=True)
    nombreAsegurado = models.CharField(max_length=80, verbose_name='Nombre del Asegurado')
    edad = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Edad')
    SEXO_OPCIONES = (
        ('M', 'Mujer'),
        ('H', 'Hombre'),
    )
    sexo = models.CharField(max_length=1, choices=SEXO_OPCIONES, blank=True, verbose_name='Sexo')
    fumador = models.BooleanField(verbose_name='Fumador')
    link = models.URLField(blank=True, verbose_name='Enlace a ID?')

    def attrs(self):
        for attr, value in self.__dict__.items():
            yield attr, value

class SeguroH(models.Model):
    tipoSeguro = OneToOneField(TipoSeguro, related_name='seguroH', null=True)

    idSeguro = models.AutoField(primary_key=True)
    TIPO_VIVIENDA_OPCIONES = (
        ("piso en primera planta", "Piso en primera planta"),
        ("piso en planta baja", "Piso en planta baja"),
        ("piso entre plantas", "Piso entre plantas"),
        ("atico", "Ático"),
        ("unifamiliar adosada", "Unifamiliar adosada"),
        ("chalet/torre", "Chalet / Torre"),
        ("casa rural de uso particular", "Casa rural de uso particular"),
        ("casa de pueblo", "Casa de pueblo"),
    )
    tipoVivienda = models.CharField(max_length=50, choices=TIPO_VIVIENDA_OPCIONES, verbose_name='Tipo de Vivenda')
    primeraResidencia = models.NullBooleanField(blank=True, null=True, verbose_name='Primera Residencia')
    metrosCuadrados = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Metros Cuadrados')
    capitalContinente = models.TextField(blank=True, default="", verbose_name='Capital Continente')
    capitalContenido = models.TextField(blank=True, default="", verbose_name='Capital Contenido')
    calle = models.CharField(max_length=100, verbose_name='Calle')
    numeroExt = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Número Ext.')
    numeroInt = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Número Int.')
    colonia = models.CharField(max_length=40, blank=True, verbose_name='Colonia')
    ciudad = models.CharField(max_length=30, blank=True, verbose_name='Ciudad')
    estado = models.CharField(max_length=19, blank=True, verbose_name='Estado')
    codigoPostal = models.CharField(max_length=5, blank=True, verbose_name='C.P.')

    def attrs(self):
        for attr, value in self.__dict__.items():
            yield attr, value

class SeguroI(models.Model):
    tipoSeguro = OneToOneField(TipoSeguro, related_name='seguroI', null=True)

    idSeguro = models.AutoField(primary_key=True)
    sumaAsegurada = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Suma Asegurada')
    planAhorro = models.CharField(max_length=20, verbose_name='Plan de Ahorro')
    identificacion = models.URLField(blank=True, verbose_name='Identificación Oficial')

    def attrs(self):
        for attr, value in self.__dict__.items():
            yield attr, value

class SeguroE(models.Model):
    tipoSeguro = OneToOneField(TipoSeguro, related_name='seguroE', null=True)

    idSeguro = models.AutoField(primary_key=True)
    nombreEmpresa = models.CharField(max_length=50, verbose_name='Nombre de Empresa')
    tipoConstruccion = models.CharField(max_length=30, verbose_name='Tipo de Construcción')
    tipoMuro = models.CharField(max_length=30, verbose_name='Tipo de Muro')
    numeroPisos = models.PositiveSmallIntegerField(verbose_name='Número de Pisos')
    numeroSotanos = models.PositiveSmallIntegerField(verbose_name='Número de Sótanos')
    direccion = models.CharField(max_length=100, verbose_name='Calle')
    numeroExt = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Número Ext.')
    numeroInt = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Número Int.')
    colonia = models.CharField(max_length=40, blank=True, verbose_name='Colonia')
    ciudad = models.CharField(max_length=30, blank=True, verbose_name='Ciudad')
    estado = models.CharField(max_length=19, blank=True, verbose_name='Estado')
    codigoPostal = models.CharField(max_length=5, blank=True, verbose_name='C.P.')

    def attrs(self):
        for attr, value in self.__dict__.items():
            yield attr, value

class SeguroEC(models.Model):
    tipoSeguro = OneToOneField(TipoSeguro, related_name='seguroEC', null=True)

    idSeguro = models.AutoField(primary_key=True)
    tipoEquipo = models.CharField(max_length=30, verbose_name='Tipo de Equipo')
    caracteristicas = models.TextField(verbose_name='Características')

    def attrs(self):
        for attr, value in self.__dict__.items():
            yield attr, value

class SeguroT(models.Model):
    tipoSeguro = OneToOneField(TipoSeguro, related_name='seguroT', null=True)

    idSeguro = models.AutoField(primary_key=True)
    tipoMedio = models.CharField(max_length=30, verbose_name='Tipo de Medio')
    bienTransportado = models.CharField(max_length=40, verbose_name='Bien Transportado')
    sumaAsegurada = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Suma Asegurada')
    ciudadOrigen = models.CharField(max_length=31, verbose_name='Ciudad Origen')
    estadoOrigen = models.CharField(max_length=19, verbose_name='Estado Origen')
    ciudadDestino = models.CharField(max_length=31, verbose_name='Ciudad Destino')
    estadoDestino = models.CharField(max_length=19, verbose_name='Estado Destino')
    tipoTrabajo = models.CharField(max_length=20, verbose_name='Tipo de Trabajo')

    def attrs(self):
        for attr, value in self.__dict__.items():
            if value is not None:
                yield attr, value

# class SeguroESP(models.Model) # Especializados
