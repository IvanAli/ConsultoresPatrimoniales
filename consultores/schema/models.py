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
    ('AP', 'Automoviles y pickups'),
    ('C', 'Camiones'),
    ('R', 'Remolques, cajas secas y adaptaciones en general'),
    ('G', 'Gastos medicos mayores'),
    ('V', 'Vida'),
    ('H', 'Hogares'),
    ('I', 'Inversion'),
    ('E', 'Empresas'),
    ('EC', 'Equipo de contratistas'),
    ('T', 'Transportes'),
    ('ESP', 'Especializados'),
)

# Create your models here.
class Persona(models.Model):
    email = models.EmailField(max_length=254)
    edad = models.PositiveSmallIntegerField(null=True)
    SEXO_OPCIONES = (
        ('M', 'Mujer'),
        ('H', 'Hombre'),
    )
    sexo = models.CharField(max_length=1, choices=SEXO_OPCIONES)
    rfc = models.CharField(max_length=13, blank=True)
    telefonoLada = models.PositiveSmallIntegerField()
    telefono = models.PositiveIntegerField()
    calle = models.CharField(max_length=50, blank=True)
    numeroExt = models.PositiveSmallIntegerField(blank=True, null=True)
    numeroInt = models.CharField(max_length=6,blank=True, null=True)
    colonia = models.CharField(max_length=40, blank=True)
    ciudad = models.CharField(max_length=30, blank=True)
    estado = models.CharField(max_length=19, blank=True)
    codigoPostal = models.PositiveIntegerField(blank=True, null=True)
    class Meta:
        abstract = True
    def __str__(self):
        return "Persona"

# def get_upload_file_name(instance, filename):
#     return "uploaded_files/%s_%s" % (str(time()).replace('.','_'),filename)

class Cliente(Persona):
    idCliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellidoPaterno = models.CharField(max_length=30)
    apellidoMaterno = models.CharField(max_length=30)
    linkRegistroRFC = models.URLField(blank=True, null=True)
    linkComprobanteDomicilio = models.FileField(null=True)
    calleFact = models.CharField(max_length=50, blank=True)
    numeroExtFact = models.PositiveSmallIntegerField(blank=True, null=True)
    numeroIntFact = models.CharField(max_length=6, blank=True, null=True)
    coloniaFact = models.CharField(max_length=40, blank=True)
    ciudadFact = models.CharField(max_length=30, blank=True)
    estadoFact = models.CharField(max_length=19, blank=True)
    codigoPostalFact = models.PositiveIntegerField(blank=True, null=True)
    def __str__(self):
        return "Cliente fisico: " + self.nombre + " " +self.apellidoPaterno + " " + self.apellidoMaterno

#Creo que seria mejor agregar como campos dentro de Cliente
class ClienteFisico(Cliente):
    def __str__(self):
        return "Cliente fisico"

#Creo que seria mejor agregar como campos dentro de Cliente
class ClienteMoral(Cliente):
    razonSocial = models.CharField(max_length=100, null=True)
    linkActaConstitutiva = models.URLField(null=True)
    linkIdRepresentante = models.URLField(null=True)
    def __str__(self):
        return "Cliente moral"

class Agente(Persona):
    userAgente = OneToOneField(User)
    claveAgente = models.IntegerField(blank=True, null=True)
    cuentaBancaria = models.CharField(max_length=34, blank=True)
    banco = models.CharField(max_length=30, blank=True)
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
    fecha = models.DateField(auto_now_add=True)

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
    nombre = models.CharField(max_length=50)
    sitioWeb = models.URLField(blank=True, null=True)
    telefonoLada = models.CharField(max_length=3)
    telefono = models.CharField(max_length=7)
    calle = models.CharField(max_length=50, blank=True)
    numeroExt = models.PositiveSmallIntegerField(blank=True)
    numeroInt = models.PositiveSmallIntegerField(blank=True, null=True)
    colonia = models.CharField(max_length=40, blank=True)
    ciudad = models.CharField(max_length=30, blank=True)
    estado = models.CharField(max_length=19, blank=True)
    codigoPostal = models.CharField(max_length=5, blank=True)
    seguros = models.ManyToManyField(TipoSeguro)

    def __str__(self):
        return self.nombre

class Comparativa(models.Model):
    idComparativa = models.AutoField(primary_key=True)
    fechaCreacion = models.DateTimeField('fecha creada', auto_now_add=True)
    fechaConclusion = models.DateTimeField('fecha concluida', blank=True, null=True)
    fechaEnvioCliente = models.DateTimeField('fecha de envio a cliente', blank=True, null=True)
    fechaEnvioTramite = models.DateTimeField('fecha de envio a tramites', blank=True, null=True)
    tipoSeguro = models.ForeignKey('TipoSeguro')
    coberturas = models.ManyToManyField('Cobertura')
    cotizacionElegida = models.OneToOneField('Cotizacion', related_name='comparativaPreferida', null=True)

class Cotizacion(models.Model):
    idCotizacion = models.AutoField(primary_key=True)
    costo = models.DecimalField(max_digits=11, decimal_places=2)
    fechaCreacion = models.DateTimeField('fecha creada', auto_now_add=True)
    FORMA_PAGO_OPCIONES = (
        (1, 'Anual'),
        (2, 'Semestral'),
        (4, 'Trimestral'),
    )
    formaPago = models.IntegerField(choices=FORMA_PAGO_OPCIONES, default=12)
    comparativa = models.ForeignKey('Comparativa', null=True)
    aseguradora = models.ForeignKey('Aseguradora')
    archivo = models.FileField(null=True, blank=True)
    elegida = models.BooleanField(default=False)
    def __str__(self):
        return "Cotizacion: " + self.idCotizacion + " de comparativa: " + self.comparativa

class AreaTramites(models.Model):
    idAreaTramites = models.AutoField(primary_key=True)
    encargado = models.CharField(max_length=60, null=True)
    email = models.EmailField(null=True)

class Poliza(models.Model):
    idPoliza = models.AutoField(primary_key=True)
    noPoliza = models.CharField(max_length=20, null=True)
    primaNeta = models.DecimalField(max_digits=11, decimal_places=2)
    fechaEmision = models.DateTimeField('fecha emitida')
    fechaInicio = models.DateTimeField('fecha de inicio')
    fechaFin = models.DateTimeField('fecha de fin', null=True)
    endosoBeneficiario = models.CharField(max_length=100, blank=True)
    caratulaPDF = models.FileField(null=True)
    comision = models.OneToOneField('Comision', null=True)
    cotizacion = models.OneToOneField('Cotizacion', null=True)
    ordenServicio = models.OneToOneField('OrdenServicio', null=True)

class Pago(models.Model):
    idPago = models.AutoField(primary_key=True)
    cantidad = models.DecimalField(max_digits=11, decimal_places=2)
    fechaPago = models.DateTimeField('fecha de pago')
    numeroPago = models.PositiveSmallIntegerField()
    comprobante = models.FileField(null=True)
    poliza = models.ForeignKey('Poliza')
    def __str__(self):
        return "Pago " + str(self.numeroPago)

class Comision(models.Model):
    idComision = models.AutoField(primary_key=True)
    cantidadComision = models.DecimalField(max_digits=11, decimal_places=2)
    fechaDeposito = models.DateTimeField(blank=True, null=True)
    asignacionComision = models.ForeignKey('AsignacionComision', null=True)
    # agente = models.ForeignKey('Agente')
    def __str__(self):
        return "Comisión " + str(self.idComision) + " de " + self.agente

class AsignacionComision(models.Model):
    idAsignacion = models.AutoField(primary_key=True)
    fechaAsignacion = models.DateTimeField('fecha de asignacion', auto_now_add=True)
    porcentaje = models.DecimalField(max_digits=4, decimal_places=2)
    seguro = models.ForeignKey('Seguro', null=True)
    aseguradora = models.ForeignKey('Aseguradora')
    def __str__(self):
        return "Asignacion de Comisión: " + self.idAsignacion + " Tipo de Seguro: " + self.tipoSeguro + " Aseguradora: " + self.aseguradora

class Contacto(models.Model):
    idContacto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellidoPaterno = models.CharField(max_length=30)
    apellidoMaterno = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, blank=True, null=True)
    telefonoLada = models.CharField(max_length=3, blank=True)
    telefono = models.CharField(max_length=7, blank=True)
    aseguradora = models.ForeignKey('Aseguradora')
    def __str__(self):
        return "Contacto: " + self.idContacto + " Aseguradora: " + self.aseguradora


class OrdenServicio(models.Model):
    idServicio = models.AutoField(primary_key=True)
    fechaServicio = models.DateTimeField('fecha de servicio', auto_now_add=True)
    fechaConclusion = models.DateTimeField(blank=True, null=True)
    agente = models.ForeignKey('Agente', null=True)
    cliente = models.ForeignKey('Cliente')
    comparativa = models.OneToOneField(Comparativa, related_name="ordenServicio", null=True)
    # poliza = models.OneToOneField(Poliza, null=True)
    def __str__ (self):
        return "Orden de Servicio: " + str(self.idServicio)

class Cobertura(models.Model):
    idCobertura = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    seguro = models.ForeignKey('Seguro', null=True)
    def __str__(self):
        return self.nombre

class CoberturaUtilizada(models.Model):
    idCoberturaUtilizada = models.AutoField(primary_key=True)
    idCobertura = models.ForeignKey(Cobertura)
    sumaAsegurada = models.CharField(max_length=30)
    deducible = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    cotizacion = models.ForeignKey('Cotizacion', null=True)

class Seguro(models.Model):
    idSeguro = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=80)

class SeguroAP(models.Model):
    tipoSeguro = OneToOneField(TipoSeguro, related_name='seguroAP', null=True)
    idSeguro = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=30, null=True)
    modelo = models.CharField(max_length=30, blank=True, null=True)
    tipoPlan = models.CharField(max_length=50, blank=True, default="")
    ano = models.PositiveSmallIntegerField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    pasajeros = models.PositiveSmallIntegerField(blank=True, null=True)
    estadoCirculacion = models.CharField(max_length=19, blank=True, null=True)
    version = models.CharField(max_length=10, blank=True)
    TRANSMISIONES_OPCIONES = (
        ("M", "Manual"),
        ("A", "Automatica"),
    )
    transmision = models.CharField(max_length=1, choices=TRANSMISIONES_OPCIONES, null=True, blank=True)

    def attrs(self):
        print("Implemented")
        for attr, value in self.__dict__.items():
            yield attr, value


class SeguroC(models.Model):
    tipoSeguro = OneToOneField(TipoSeguro, related_name='seguroC', null=True)
    idSeguro = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=30, null=True, blank=True)
    modelo = models.CharField(max_length=30, blank=True, null=True)
    ano = models.PositiveSmallIntegerField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    pasajeros = models.PositiveSmallIntegerField(blank=True, null=True)
    unidad = models.PositiveSmallIntegerField()
    TRANSMISIONES_OPCIONES = (
        ("M", "Manual"),
        ("A", "Automatica"),
    )
    transmision = models.CharField(max_length=1, choices=TRANSMISIONES_OPCIONES)

    def attrs(self):
        for attr, value in self.__dict__.items():
            yield attr, value

class SeguroR(models.Model):
    tipoSeguro = OneToOneField(TipoSeguro, related_name='seguroR', null=True)

    idSeguro = models.AutoField(primary_key=True)
    capacidad = models.CharField(max_length=15)
    ejes = models.PositiveSmallIntegerField()
    descripcion = models.TextField(blank=True, null=True)

    def attrs(self):
        for attr, value in self.__dict__.items():
            yield attr, value

class SeguroG(models.Model):
    tipoSeguro = OneToOneField(TipoSeguro, related_name='seguroG', null=True)

    idSeguro = models.AutoField(primary_key=True)
    nombreAsegurado = models.CharField(max_length=80)
    coaseguro = models.DecimalField(max_digits=11, decimal_places=2)
    topeCoaseguro = models.DecimalField(max_digits=11, decimal_places=2)

    def attrs(self):
        for attr, value in self.__dict__.items():
            yield attr, value

class SeguroV(models.Model):
    tipoSeguro = OneToOneField(TipoSeguro, related_name='seguroV', null=True)

    idSeguro = models.AutoField(primary_key=True)
    nombreAsegurado = models.CharField(max_length=80)
    edad = models.PositiveSmallIntegerField(null=True, blank=True)
    SEXO_OPCIONES = (
        ('M', 'Mujer'),
        ('H', 'Hombre'),
    )
    sexo = models.CharField(max_length=1, choices=SEXO_OPCIONES, blank=True)
    fumador = models.BooleanField()
    link = models.URLField(blank=True)

    def attrs(self):
        for attr, value in self.__dict__.items():
            yield attr, value

class SeguroH(models.Model):
    tipoSeguro = OneToOneField(TipoSeguro, related_name='seguroH', null=True)

    idSeguro = models.AutoField(primary_key=True)
    codigoPostal = models.CharField(max_length=5)
    TIPO_VIVIENDA_OPCIONES = (
        ("piso en primera planta", "Piso en primera planta"),
        ("piso en planta baja", "Piso en planta baja"),
        ("piso entre plantas", "Piso entre plantas"),
        ("atico", "Atico"),
        ("unifamiliar adosada", "Unifamiliar adosada"),
        ("chalet/torre", "Chalet / Torre"),
        ("casa rural de uso particular", "Casa rural de uso particular"),
        ("casa de pueblo", "Casa de pueblo"),
    )
    tipoVivienda = models.CharField(max_length=50, choices=TIPO_VIVIENDA_OPCIONES)
    primeraResidencia = models.NullBooleanField(blank=True, null=True)
    metrosCuadrados = models.PositiveSmallIntegerField(blank=True, null=True)
    capitalContinente = models.TextField(blank=True, default="")
    capitalContenido = models.TextField(blank=True, default="")

    def attrs(self):
        for attr, value in self.__dict__.items():
            yield attr, value

class SeguroI(models.Model):
    tipoSeguro = OneToOneField(TipoSeguro, related_name='seguroI', null=True)

    idSeguro = models.AutoField(primary_key=True)
    sumaAsegurada = models.DecimalField(max_digits=11, decimal_places=2)
    planAhorro = models.CharField(max_length=20)
    identificacion = models.URLField(blank=True)

    def attrs(self):
        for attr, value in self.__dict__.items():
            yield attr, value

class SeguroE(models.Model):
    tipoSeguro = OneToOneField(TipoSeguro, related_name='seguroE', null=True)

    idSeguro = models.AutoField(primary_key=True)
    nombreEmpresa = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    tipoConstruccion = models.CharField(max_length=30)
    tipoMuro = models.CharField(max_length=30)
    tipoConstruccion = models.CharField(max_length=30)
    numeroPisos = models.PositiveSmallIntegerField()
    numeroSotanos = models.PositiveSmallIntegerField()
    numeroExt = models.PositiveSmallIntegerField(blank=True, null=True)
    numeroInt = models.PositiveSmallIntegerField(blank=True, null=True)
    colonia = models.CharField(max_length=40, blank=True)
    ciudad = models.CharField(max_length=30, blank=True)
    estado = models.CharField(max_length=19, blank=True)
    codigoPostal = models.CharField(max_length=5, blank=True)

    def attrs(self):
        for attr, value in self.__dict__.items():
            yield attr, value

class SeguroEC(models.Model):
    tipoSeguro = OneToOneField(TipoSeguro, related_name='seguroEC', null=True)

    idSeguro = models.AutoField(primary_key=True)
    tipoEquipo = models.CharField(max_length=30)
    caracteristicas = models.TextField()

    def attrs(self):
        for attr, value in self.__dict__.items():
            yield attr, value

class SeguroT(models.Model):
    tipoSeguro = OneToOneField(TipoSeguro, related_name='seguroT', null=True)

    idSeguro = models.AutoField(primary_key=True)
    tipoMedio = models.CharField(max_length=30)
    bienTransportado = models.CharField(max_length=40)
    sumaAsegurada = models.DecimalField(max_digits=11, decimal_places=2)
    ciudadOrigen = models.CharField(max_length=31)
    estadoOrigen = models.CharField(max_length=19)
    ciudadDestino = models.CharField(max_length=31)
    estadoDestino = models.CharField(max_length=19)
    tipoTrabajo = models.CharField(max_length=20)

    def attrs(self):
        for attr, value in self.__dict__.items():
            if value is not None:
                yield attr, value

# class SeguroESP(models.Model) # Especializados
