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

# Create your models here.
class Persona(models.Model):
    # nombre = models.CharField(max_length=40, null=True, blank=False)
    # apellidoPaterno = models.CharField(max_length=30, null=True)
    # apellidoMaterno = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    edad = models.PositiveSmallIntegerField(null=True)
    SEXO_OPCIONES = (
        (None, '-'),
        ('M', 'Mujer'),
        ('H', 'Hombre'),
        ('O', 'Otro'),
        )
    sexo = models.CharField(max_length=1, choices=SEXO_OPCIONES, default='M')
    rfc = models.CharField(max_length=13, null=True)
    telefonoLada = models.CharField(max_length=3, null=True)
    telefono = models.CharField(max_length=7, null=True)
    calle = models.CharField(max_length=50, blank=True, null=True)
    numeroExt = models.PositiveSmallIntegerField(blank=True, null=True)
    numeroInt = models.PositiveSmallIntegerField(blank=True, null=True)
    colonia = models.CharField(max_length=40, blank=True, null=True)
    ciudad = models.CharField(max_length=30, blank=True, null=True)
    estado = models.CharField(max_length=19, blank=True, null=True)
    codigoPostal = models.CharField(max_length=5, blank=True, null=True)
    class Meta:
        abstract = True

class Cliente(Persona):
    nombre = models.CharField(max_length=40, null=True, blank=False)
    apellidoPaterno = models.CharField(max_length=30, null=True)
    apellidoMaterno = models.CharField(max_length=30, null=True)
    linkRegistroRFC = models.URLField(null=True)
    linkComprobanteDomicilio = models.URLField(null=True)
    calleFact = models.CharField(max_length=50, null=True)
    numeroExtFact = models.PositiveSmallIntegerField(null=True)
    numeroIntFact = models.PositiveSmallIntegerField(blank=True, null=True)
    coloniaFact = models.CharField(max_length=40, null=True)
    ciudadFact = models.CharField(max_length=30, null=True)
    estadoFact = models.CharField(max_length=19, null=True)
    codigoPostalFact = models.CharField(max_length=5, null=True)

class ClienteFisico(Cliente):
    def __str__(self):
        return "Cliente fisico"

class ClienteMoral(Cliente):
    razonSocial = models.CharField(max_length=100, null=True)
    linkActaConstitutiva = models.URLField(null=True)
    linkIdRepresentante = models.URLField(null=True)

class Agente(Persona):
    userAgente = OneToOneField(User)
    claveAgente = models.IntegerField(blank=True, null=True)
    cuentaBancaria = models.CharField(max_length=34, null=True)
    banco = models.CharField(max_length=30, null=True)

    # many to many relationship with Cliente
    clientes = models.ManyToManyField(Cliente, through='OrdenServicio')

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

class Aseguradora(models.Model):
    idAseguradora = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=True)
    sitioWeb = models.URLField(blank=True, null=True)
    telefonoLada = models.CharField(max_length=3, null=True)
    telefono = models.CharField(max_length=7, null=True)
    ### Estos campos son opcionales?
    calle = models.CharField(max_length=50, blank=True, null=True)
    numeroExt = models.PositiveSmallIntegerField(blank=True, null=True)
    numeroInt = models.PositiveSmallIntegerField(blank=True, null=True)
    colonia = models.CharField(max_length=40, blank=True, null=True)
    ciudad = models.CharField(max_length=30, blank=True, null=True)
    estado = models.CharField(max_length=19, blank=True, null=True)
    codigoPostal = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return "Aseguradora: " + self.nombre

class DatoTipoSeguro(models.Model):
    llave = models.CharField(max_length=40, primary_key=True)
    valor = models.CharField(max_length=80)
    class Meta:
        unique_together = ("llave", "valor")
    def __str__(self):
        return self.llave + ": " + self.valor


class TipoSeguro(models.Model):

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
    idTipoSeguro = models.CharField(max_length=3, choices=SEGUROS_OPCIONES, primary_key=True)
    datos = models.ManyToManyField(DatoTipoSeguro)
    aseguradora = models.ForeignKey(Aseguradora, null=True)

    class Meta:
        unique_together = ("idTipoSeguro", "aseguradora")

    def __str__(self):
        return "Seguro: " + self.idTipoSeguro


class DatoCobertura(models.Model):
    llave = models.CharField(max_length=40, primary_key=True)
    valor = models.CharField(max_length=80)
    class Meta:
        unique_together = ("llave", "valor")
    def __str__(self):
        return self.llave + ": " + self.valor

class Cobertura(models.Model):
    """
        Considerar que la Cobertura puede tambien tener muchos datos y la descripcion
        puede que no sea suficiente

        Se creo DatoCobertura para solucionar esto.

    """

    idCobertura = models.AutoField(primary_key=True)
    nombreCobertura = models.CharField(max_length=50, null=True)
    tipoSeguro = models.ForeignKey(TipoSeguro, null=True)
    datos = models.ManyToManyField(DatoCobertura)

    def __str__(self):
        return "Cobertura: " + self.nombreCobertura


class Comparativa(models.Model):
    idComparativa = models.AutoField(primary_key=True)
    numeroCotizaciones = models.PositiveIntegerField(null=True)
    fechaCreacion = models.DateTimeField('fecha creada', auto_now_add=True, null=True)
    fechaConclusion = models.DateTimeField('fecha concluida', blank=True, null=True)
    fechaEnvio = models.DateTimeField('fecha de envio', blank=True, null=True)

    ordenServicio = models.ForeignKey('OrdenServicio', null=True)
    # cliente = models.ForeignKey(Cliente, null=True)
    # agente = models.ForeignKey(Agente, null=True)

    def __str__(self):
        return "Comparativa: " + self.idComparativa + " Cliente: " + self.cliente + " Agente: " + self.agente

class Comision(models.Model):
    idComision = models.AutoField(primary_key=True)
    cantidadComision = models.DecimalField(max_digits=11, decimal_places=2, null=True)
    fechaDeposito = models.DateTimeField(null=True)
    # asignacionComision = models.ForeignKey(AsignacionComision)
    agente = models.ForeignKey(Agente, null=True)
    def __str__(self):
        return "Comisión " + self.idComision + " de Agente " + self.agente

class Cotizacion(models.Model):
    idCotizacion = models.AutoField(primary_key=True)
    costo = models.DecimalField(max_digits=11, decimal_places=2, null=True)
    fechaCreacion = models.DateTimeField('fecha creada', null=True)
    FORMA_PAGO_OPCIONES = (
        (12, 'Anual'),
        (6, 'Semestral'),
        (3, 'Trimestral'),
    )
    formaPago = models.IntegerField(choices=FORMA_PAGO_OPCIONES, default=12, null=True)
    comparativa = models.ForeignKey(Comparativa, null=True)
    aseguradora = models.ForeignKey(Aseguradora, null=True)
    def __str__(self):
        return "Cotizacion: " + self.idCotizacion + " de comparativa: " + self.comparativa

class Poliza(models.Model):
    idPoliza = models.AutoField(primary_key=True)
    primaNeta = models.DecimalField(max_digits=11, decimal_places=2, null=True)
    fechaEmision = models.DateTimeField('fecha emitida', null=True)
    fechaInicio = models.DateTimeField('fecha de inicio', null=True)
    fechaFin = models.DateTimeField('fecha de fin', null=True)
    endosoBeneficiario = models.CharField(max_length=50, null=True)
    linkCaratulaPDF = models.URLField(max_length=200, null=True)
    # cliente = models.ForeignKey(Cliente, null=True)
    # agente = models.ForeignKey(Agente, null=True)
    comision = models.OneToOneField(Comision, null=True)
    # aseguradora = models.ForeignKey(Aseguradora, null=True)
    cotizacion = models.OneToOneField(Cotizacion, null=True)
    def __str__(self):
        return "Póliza: " + self.idPoliza + "Cliente: " + self.cliente + "Agente: " + self.agente

class Pago(models.Model):
    idPago = models.AutoField(primary_key=True)
    cantidad = models.DecimalField(max_digits=11, decimal_places=2, null=True)
    fechaPago = models.DateTimeField('fecha de pago', null=True)
    numeroPago = models.PositiveSmallIntegerField(null=True)
    poliza = models.ForeignKey(Poliza, null=True)
    def __str__(self):
        return "Pago " + self.numeroPago + " de Poliza " + self.poliza


class AsignacionComision(models.Model):
    idAsignacion = models.AutoField(primary_key=True)
    fechaAsignacion = models.DateTimeField('fecha de asignacion')
    porcentaje = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    tipoSeguro = models.ForeignKey(TipoSeguro, null=True)
    aseguradora = models.ForeignKey(Aseguradora, null=True)
    comision = models.ForeignKey(Comision, null=True)
    def __str__(self):
        return "Asignacion de Comisión: " + self.idAsignacion + " Tipo de Seguro: " + self.tipoSeguro + " Aseguradora: " + self.aseguradora

class Contacto(models.Model):
    idContacto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, null=True)
    apellidoPaterno = models.CharField(max_length=30, null=True)
    apellidoMaterno = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=254, null=True)
    telefonoLada = models.CharField(max_length=3, blank=True, null=True)
    telefono = models.CharField(max_length=7, blank=True, null=True)
    aseguradora = models.ForeignKey(Aseguradora, null=True)
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
    cliente = models.ForeignKey(Cliente, null=True)
    agente = models.ForeignKey(Agente, null=True)
    tipoSeguro = models.ForeignKey(TipoSeguro, null=True)
    ### foreign key is under Comparativa
    # comparativa = models.OneToOneField(Comparativa, null=True)
    poliza = models.OneToOneField(Poliza, null=True)
    def __str__ (self):
        return "Orden de Servicio: " + self.idServicio + " Cliente: " + self.cliente + " Agente: " + self.agente;
