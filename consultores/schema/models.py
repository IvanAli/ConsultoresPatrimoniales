from django.db import models

# Create your models here.
class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellidoPaterno = models.CharField(max_length=20)
    apellidoMaterno = models.CharField(max_length=20)
    email = models.EmailField(max_length=60)
    telefonoLada = models.CharField(max_length=3)
    telefono = models.CharField(max_length=7)
    calle = models.CharField(max_length=50)
    numeroExt = models.IntegerField()
    numeroInt = models.IntegerField(blank=True)
    colonia = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=25)
    estado = models.CharField(max_length=25)
    codigoPostal = models.IntegerField()
    usuario = models.CharField(max_length=30)
    contrasena = models.CharField(max_length=30)
    class Meta:
        abstract = True
    def __str__(self):
        return nombre + apellidoPaterno + apellidoMaterno

class Cliente(Usuario):
    linkRegistroRFC = models.URLField()
    linkComprobanteDomicilio = models.URLField()

class ClienteFisica(Cliente):
    calleFact = models.CharField(max_length=50)
    numeroExtFact = models.IntegerField()
    numeroIntFact = models.IntegerField(blank=True)
    coloniaFact = models.CharField(max_length=50)
    ciudadFact = models.CharField(max_length=25)
    estadoFact = models.CharField(max_length=25)
    codigoPostalFact = models.IntegerField()

class ClienteMoral(Cliente):
    razonSocial = models.CharField(max_length=100)
    linkActaConstitutiva = models.URLField()
    linkIdRepresentante = models.URLField()

class Agente(Usuario):
    claveAgente = models.IntegerField()
    cuentaBancaria = models.CharField(max_length=34)
    banco = models.CharField(max_length=30)

class TipoSeguro(models.Model):
    idTipoSeguro = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
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
    # idTipoSeguro = models.CharField(max_length=3, choices=SEGURO_OPCIONES, primary_key=True)

class Aseguradora(models.Model):
    idAseguradora = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    sitioWeb = models.TextField(blank=True)
    telefonoLada = models.CharField(max_length=3)
    telefono = models.CharField(max_length=7)
    calle = models.CharField(max_length=50)
    numeroExt = models.IntegerField()
    numeroInt = models.IntegerField(blank=True)
    colonia = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=25)
    estado = models.CharField(max_length=25)
    codigoPostal = models.IntegerField()

class OrdenServicio(models.Model):
    idServicio = models.AutoField(primary_key=True)
    fechaServicio = models.DateTimeField('fecha de servicio')
    cliente = models.ForeignKey(Cliente)
    agente = models.ForeignKey(Agente)

class Comparativa(models.Model):
    idComparativa = models.AutoField(primary_key=True)
    tipoSeguro = models.ForeignKey(TipoSeguro);
    numeroCotizaciones = models.IntegerField()
    fechaCreacion = models.DateTimeField('fecha creada')
    fechaConclusion = models.DateTimeField('fecha concluida')
    fechaEnvio = models.DateTimeField('fecha de envio')

class Cotizacion(models.Model):
    idCotizacion = models.AutoField(primary_key=True)
    comparativa = models.ForeignKey(Comparativa)
    aseguradora = models.ForeignKey(Aseguradora)
    costo = models.DecimalField(max_digits=3, decimal_places=1)
    fechaCreacion = models.DateTimeField('fecha creada')
    FORMA_PAGO_OPCIONES = (
        (12, 'Anual'),
        (6, 'Semestral'),
        (3, 'Trimestral'),
    )
    formaPago = models.IntegerField(choices=FORMA_PAGO_OPCIONES, default=12)

class Dato(models.Model):
    idDato = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

class Cobertura(models.Model):
    idCobertura = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    porcentajeCobertura = models.DecimalField(max_digits=3, decimal_places=1)

class Contacto(models.Model): # should it inherit from Persona?
    idContacto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellidoPaterno = models.CharField(max_length=20)
    apellidoMaterno = models.CharField(max_length=20)
    email = models.CharField(max_length=60)
    telefonoLada = models.CharField(max_length=3)
    telefono = models.CharField(max_length=7)

class AsignacionComision(models.Model):
    idAsignacion = models.AutoField(primary_key=True)
    tipoSeguro = models.ForeignKey(TipoSeguro)
    aseguradora = models.ForeignKey(Aseguradora)
    fechaAsignacion = models.DateTimeField('fecha de asignacion')
    porcentaje = models.DecimalField(max_digits=3, decimal_places=1)

class Comision(models.Model):
    idComision = models.AutoField(primary_key=True)
    cantidadComision = models.DecimalField(max_digits=3, decimal_places=1)
    fechaDeposito = models.DateTimeField(null=True)
    asignacionComision = models.ForeignKey(AsignacionComision)

class Poliza(models.Model):
    idPoliza = models.AutoField(primary_key=True)
    servicio = models.ForeignKey(OrdenServicio)
    primaNeta = models.DecimalField(max_digits=3, decimal_places=1)
    fechaEmision = models.DateTimeField('fecha emitida')
    fechaInicio = models.DateTimeField('fecha de inicio')
    fechaFin = models.DateTimeField('fecha de fin')
    endosoBeneficiario = models.CharField(max_length=50)
    linkCaratulaPDF = models.URLField(max_length=200)
    # fechaPagoComision
    comision = models.ForeignKey(Comision)


class Pago(models.Model):
    idPago = models.AutoField(primary_key=True)
    cantidad = models.DecimalField(max_digits=3, decimal_places=1)
    fechaPago = models.DateTimeField('fecha de pago')
