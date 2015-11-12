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
    telefonoLada = models.CharField(max_length=3)
    telefono = models.CharField(max_length=7)
    calle = models.CharField(max_length=50, blank=True)
    numeroExt = models.PositiveSmallIntegerField(blank=True, null=True)
    numeroInt = models.PositiveSmallIntegerField(blank=True, null=True)
    colonia = models.CharField(max_length=40, blank=True)
    ciudad = models.CharField(max_length=30, blank=True)
    estado = models.CharField(max_length=19, blank=True)
    codigoPostal = models.CharField(max_length=5, blank=True)
    class Meta:
        abstract = True
    def __str__(self):
        return "Persona"

class Cliente(Persona):
    idCliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellidoPaterno = models.CharField(max_length=30)
    apellidoMaterno = models.CharField(max_length=30)
    linkRegistroRFC = models.URLField(blank=True, null=True)
    linkComprobanteDomicilio = models.URLField(blank=True, null=True)
    calleFact = models.CharField(max_length=50, blank=True)
    numeroExtFact = models.PositiveSmallIntegerField(blank=True, null=True)
    numeroIntFact = models.PositiveSmallIntegerField(blank=True, null=True)
    coloniaFact = models.CharField(max_length=40, blank=True)
    ciudadFact = models.CharField(max_length=30, blank=True)
    estadoFact = models.CharField(max_length=19, blank=True)
    codigoPostalFact = models.CharField(max_length=5, blank=True)
    def __str__(self):
        return "Cliente fisico: " + self.nombre + " " +self.apellidoPaterno + " " + self.apellidoMaterno

class ClienteFisico(Cliente):
    def __str__(self):
        return "Cliente fisico"

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
    clientes = models.ManyToManyField(Cliente)

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


class TipoSeguro(models.Model):
    tipo = models.CharField(max_length=3, choices=SEGUROS_OPCIONES, null=True)
    idTipoSeguro = models.AutoField(primary_key=True)

    def __str__(self):
    	return "Seguro: " + self.idTipoSeguro

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
        return "Aseguradora: " + self.nombre
"""
class SegurosOfertados(models.Model):
    aseguradora = models.ForeignKey('Aseguradora')
    tipoSeguro = models.ForeignKey('TipoSeguro')

    class Meta:
        unique_together = ("aseguradora", "tipoSeguro")
"""

class Comparativa(models.Model):
    idComparativa = models.AutoField(primary_key=True)
    fechaCreacion = models.DateTimeField('fecha creada', auto_now_add=True)
    fechaConclusion = models.DateTimeField('fecha concluida', blank=True, null=True)
    fechaEnvio = models.DateTimeField('fecha de envio', blank=True, null=True)
    tipoSeguro = models.ForeignKey('TipoSeguro')
    coberturas = models.ManyToManyField('Cobertura')

### HACE FALTA RESOLVER LO DE COBERTURAS
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
    def __str__(self):
        return "Cotizacion: " + self.idCotizacion + " de comparativa: " + self.comparativa

class Poliza(models.Model):
    idPoliza = models.AutoField(primary_key=True)
    primaNeta = models.DecimalField(max_digits=11, decimal_places=2)
    fechaEmision = models.DateTimeField('fecha emitida')
    fechaInicio = models.DateTimeField('fecha de inicio')
    fechaFin = models.DateTimeField('fecha de fin')
    endosoBeneficiario = models.CharField(max_length=100, blank=True)
    linkCaratulaPDF = models.URLField(max_length=200)
    comision = models.OneToOneField('Comision')
    cotizacion = models.OneToOneField('Cotizacion')
    ordenServicio = models.OneToOneField('OrdenServicio')

class Pago(models.Model):
    idPago = models.AutoField(primary_key=True)
    cantidad = models.DecimalField(max_digits=11, decimal_places=2)
    fechaPago = models.DateTimeField('fecha de pago', auto_now_add=True)
    numeroPago = models.PositiveSmallIntegerField()
    poliza = models.ForeignKey('Poliza')
    def __str__(self):
        return "Pago " + self.numeroPago + " de Poliza " + self.poliza

class Comision(models.Model):
    idComision = models.AutoField(primary_key=True)
    cantidadComision = models.DecimalField(max_digits=11, decimal_places=2)
    fechaDeposito = models.DateTimeField(blank=True, null=True)
    asignacionComision = models.ForeignKey('AsignacionComision', null=True)
    agente = models.ForeignKey('Agente')
    def __str__(self):
        return "Comisión " + self.idComision + " de Agente " + self.agente

class AsignacionComision(models.Model):
    idAsignacion = models.AutoField(primary_key=True)
    fechaAsignacion = models.DateTimeField('fecha de asignacion', auto_now_add=True)
    porcentaje = models.DecimalField(max_digits=4, decimal_places=2)
    tipoSeguro = models.ForeignKey('TipoSeguro')
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

"""
class CoberturasUtilizadas(models.Model):
    poliza = models.ForeignKey(Poliza, null=True)
    cobertura = models.ForeignKey(Cobertura, null=True)
    def __str__(self):
        return "Cobertura " + self.cobertura + " utilizada en Poliza " + self.poliza
"""

class OrdenServicio(models.Model):
    idServicio = models.AutoField(primary_key=True)
    fechaServicio = models.DateTimeField('fecha de servicio', auto_now_add=True)
    fechaConclusion = models.DateTimeField(blank=True, null=True)
    # agente = models.ForeignKey('Agente')
    cliente = models.ForeignKey('Cliente')
    comparativa = models.OneToOneField(Comparativa, null=True)
    # poliza = models.OneToOneField(Poliza, null=True)
    def __str__ (self):
        return "Orden de Servicio: " + str(self.idServicio)

class Cobertura(models.Model):
    idCobertura = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=3, choices=SEGUROS_OPCIONES, null=True)

class CoberturaUtilizada(models.Model):
    idCoberturaUtilizada = models.AutoField(primary_key=True)
    idCobertura = models.ForeignKey(Cobertura)
    sumaAsegurada = models.CharField(max_length=30)
    deducible = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    cotizacion = models.ForeignKey('Cotizacion', null=True)

class SeguroAP(TipoSeguro):
    def __init__(self, *args, **kwargs):
        super(SeguroAP, self).__init__(*args, **kwargs)
        self.tipo = 'AP'

    idSeguro = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=30, null=True, blank=True)
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

    def __str__(self):
        return "SeguroAP" + self.idSeguro

class SeguroC(TipoSeguro):
    def __init__(self, *args, **kwargs):
        super(SeguroC, self).__init__(*args, **kwargs)
        self.tipo = 'C'

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

class SeguroR(TipoSeguro):
    def __init__(self, *args, **kwargs):
        super(SeguroR, self).__init__(*args, **kwargs)
        self.tipo = 'R'

    idSeguro = models.AutoField(primary_key=True)
    capacidad = models.CharField(max_length=15)
    ejes = models.PositiveSmallIntegerField()
    descripcion = models.TextField(blank=True, null=True)

class SeguroG(TipoSeguro):
    def __init__(self, *args, **kwargs):
        super(SeguroG, self).__init__(*args, **kwargs)
        self.tipo = 'G'

    idSeguro = models.AutoField(primary_key=True)
    nombreAsegurado = models.CharField(max_length=80)
    coaseguro = models.DecimalField(max_digits=11, decimal_places=2)
    topeCoaseguro = models.DecimalField(max_digits=11, decimal_places=2)
    # preferencias = models.ForeignKey(Cobertura)

class SeguroV(TipoSeguro):
    def __init__(self, *args, **kwargs):
        super(SeguroV, self).__init__(*args, **kwargs)
        self.tipo = 'V'
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

class SeguroH(TipoSeguro):
    def __init__(self, *args, **kwargs):
        super(SeguroH, self).__init__(*args, **kwargs)
        self.tipo = 'H'
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

class SeguroI(TipoSeguro):
    def __init__(self, *args, **kwargs):
        super(SeguroI, self).__init__(*args, **kwargs)
        self.tipo = 'I'
    idSeguro = models.AutoField(primary_key=True)
    sumaAsegurada = models.DecimalField(max_digits=11, decimal_places=2)
    planAhorro = models.CharField(max_length=20)
    identificacion = models.URLField(blank=True)

class SeguroE(TipoSeguro):
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

class SeguroEC(TipoSeguro):
    idSeguro = models.AutoField(primary_key=True)
    tipoEquipo = models.CharField(max_length=30)
    caracteristicas = models.TextField()

class SeguroT(TipoSeguro):
    idSeguro = models.AutoField(primary_key=True)
    tipoMedio = models.CharField(max_length=30)
    bienTransportado = models.CharField(max_length=40)
    sumaAsegurada = models.DecimalField(max_digits=11, decimal_places=2)
    ciudadOrigen = models.CharField(max_length=31)
    estadoOrigen = models.CharField(max_length=19)
    ciudadDestino = models.CharField(max_length=31)
    estadoDestino = models.CharField(max_length=19)
    tipoTrabajo = models.CharField(max_length=20)

# class SeguroESP(models.Model) # Especializados
