from django.db import models
"""
 REVISAR IMPLEMENTACION DE URL PARA CADA CLASE
    #def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse()
"""

# Create your models here.
class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=30, null=True)
    contrasena = models.CharField(max_length=30, null=True)
    nombre = models.CharField(max_length=40, null=True)
    apellidoPaterno = models.CharField(max_length=30, null=True)
    apellidoMaterno = models.CharField(max_length=30, null=True)
    edad = models.PositiveSmallIntegerField(null=True)
    SEXO_OPCIONES = (
        (None, '-'),
        ('M', 'Mujer'),
        ('H', 'Hombre'),
        ('O', 'Otro'),
        )
    sexo = models.CharField(max_length=1, choices=SEXO_OPCIONES, default=None)
    rfc = models.CharField(max_length=13, null=True)
    email = models.EmailField(max_length=254, null=True)
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
    def __unicode__(self):
        return "Usuario: " + self.nombre +" "+ self.apellidoPaterno +" "+ self.apellidoMaterno

class Cliente(Usuario):
    linkRegistroRFC = models.URLField(null=True)
    linkComprobanteDomicilio = models.URLField(null=True)
    calleFact = models.CharField(max_length=50, null=True)
    numeroExtFact = models.PositiveSmallIntegerField(null=True)
    numeroIntFact = models.PositiveSmallIntegerField(blank=True, null=True)
    coloniaFact = models.CharField(max_length=40, null=True)
    ciudadFact = models.CharField(max_length=30, null=True)
    estadoFact = models.CharField(max_length=19, null=True)
    codigoPostalFact = models.CharField(max_length=5, null=True)
    def __unicode__(self):
        return "Cliente: " + self.nombre +" "+ self.apellidoPaterno +" "+ self.apellidoMaterno

class ClienteFisico(Cliente):
    def __unicode__(self):
        return "Persona Física: " + self.nombre + " " + self.apellidoPaterno + " " + self.apellidoMaterno

class ClienteMoral(Cliente):
    razonSocial = models.CharField(max_length=100, null=True)
    linkActaConstitutiva = models.URLField(null=True)
    linkIdRepresentante = models.URLField(null=True)
    def __unicode__(self):
        return "Persona Moral: " + self.nombre +" "+ self.apellidoPaterno +" "+ self.apellidoMaterno

class Agente(Usuario):
    claveAgente = models.IntegerField(blank=True, null=True)
    cuentaBancaria = models.CharField(max_length=34, null=True)
    banco = models.CharField(max_length=30, null=True)
    def __unicode__(self):
        return "Agente: " + self.nombre +" "+ self.apellidoPaterno +" "+ self.apellidoMaterno

class TipoSeguro(models.Model):
    ### No será mejor poner el ID como las iniciales de SEGUROS_OPCIONES? Si
    # idTipoSeguro = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=True)
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
    def __unicode__(self):
        return "Seguro: " + self.tipoSeguro

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
    def __unicode__(self):
        return "Aseguradora: " + self.nombre

class Comparativa(models.Model):
    idComparativa = models.AutoField(primary_key=True)
    numeroCotizaciones = models.PositiveIntegerField(null=True)
    fechaCreacion = models.DateTimeField('fecha creada', auto_now_add=True, null=True)
    fechaConclusion = models.DateTimeField('fecha concluida', blank=True, null=True)
    fechaEnvio = models.DateTimeField('fecha de envio', blank=True, null=True)
    cliente = models.ForeignKey(Cliente, null=True)
    agente = models.ForeignKey(Agente, null=True)
    def __unicode__(self):
        return "Comparativa: " + self.idComparativa + " Cliente: " + self.cliente + " Agente: " + self.agente

class Comision(models.Model):
    idComision = models.AutoField(primary_key=True)
    cantidadComision = models.DecimalField(max_digits=11, decimal_places=2, null=True)
    fechaDeposito = models.DateTimeField(null=True)
    # asignacionComision = models.ForeignKey(AsignacionComision)
    agente = models.ForeignKey(Agente, null=True)
    def __unicode__(self):
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
    def __unicode__(self):
        return "Cotizacion: " + self.idCotizacion + " de comparativa: " + self.comparativa

class Poliza(models.Model):
    idPoliza = models.AutoField(primary_key=True)
    primaNeta = models.DecimalField(max_digits=11, decimal_places=2, null=True)
    fechaEmision = models.DateTimeField('fecha emitida', null=True)
    fechaInicio = models.DateTimeField('fecha de inicio', null=True)
    fechaFin = models.DateTimeField('fecha de fin', null=True)
    endosoBeneficiario = models.CharField(max_length=50, null=True)
    linkCaratulaPDF = models.URLField(max_length=200, null=True)
    cliente = models.ForeignKey(Cliente, null=True)
    agente = models.ForeignKey(Agente, null=True)
    comision = models.ForeignKey(Comision, null=True)
    aseguradora = models.ForeignKey(Aseguradora, null=True)
    def __unicode__(self):
        return "Póliza: " + self.idPoliza + "Cliente: " + self.cliente + "Agente: " + self.agente

class Pago(models.Model):
    idPago = models.AutoField(primary_key=True)
    cantidad = models.DecimalField(max_digits=11, decimal_places=2, null=True)
    fechaPago = models.DateTimeField('fecha de pago', null=True)
    numeroPago = models.PositiveSmallIntegerField(null=True)
    poliza = models.ForeignKey(Poliza, null=True)
    def __unicode__(self):
        return "Pago " + self.numeroPago + " de Poliza " + self.poliza


class AsignacionComision(models.Model):
    idAsignacion = models.AutoField(primary_key=True)
    fechaAsignacion = models.DateTimeField('fecha de asignacion')
    porcentaje = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    tipoSeguro = models.ForeignKey(TipoSeguro, null=True)
    aseguradora = models.ForeignKey(Aseguradora, null=True)
    comision = models.ForeignKey(Comision, null=True)
    def __unicode__(self):
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
    def __unicode__(self):
        return "Contacto: " + self.idContacto + " Aseguradora: " + self.aseguradora

class SegurosOfertados(models.Model):
    aseguradora = models.ForeignKey(Aseguradora)
    seguro = models.ForeignKey(TipoSeguro)
    def __unicode__(self):
        return "Aseguradora " + self.aseguradora + " oferta Seguro " + self.seguro

class Dato(models.Model):
    idDato = models.AutoField(primary_key=True)
    nombreDato = models.CharField(max_length=50, null=True)
    ### Está bien modelado esto? No estoy seguro cómo modelarlo, lo comentamos el lunes
    tipoDato = models.CharField(max_length=50, null=True)
    descripcion = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return "Dato: " + self.nombreDato + " Tipo: " + self.tipoDato

class DatosNecesitados(models.Model):
    seguro = models.ForeignKey(TipoSeguro, null=True)
    dato = models.ForeignKey(Dato, null=True)
    def __unicode__(self):
        return "Dato " + self.dato + " es necesario en Seguro " + self.seguro

class Cobertura(models.Model):
    idCobertura = models.AutoField(primary_key=True)
    nombreCobertura = models.CharField(max_length=50, null=True)
    descripcion = models.TextField(null=True)
    porcentajeCobertura = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    seguro = models.ForeignKey(TipoSeguro, null=True)
    def __unicode__(self):
        return "Cobertura: " + self.nombreCobertura + " pertenece a Seguro: " + self.seguro

class CoberturasRequeridas(models.Model):
    comparativa = models.ForeignKey(Comparativa, null=True)
    cobertura = models.ForeignKey(Cobertura, null=True)
    def __unicode__(self):
        return "Cobertura " + self.cobertura + " requerida en Comparativa " + self.comparativa

class CoberturasUtilizadas(models.Model):
    poliza = models.ForeignKey(Poliza, null=True)
    cobertura = models.ForeignKey(Cobertura, null=True)
    def __unicode__(self):
        return "Cobertura " + self.cobertura + " utilizada en Poliza " + self.poliza

class OrdenServicio(models.Model):
    idServicio = models.AutoField(primary_key=True)
    # fechaServicio = models.DateTimeField(auto_now_add=True, 'fecha de servicio')
    fechaConclusion = models.DateTimeField(blank=True, null=True)
    cliente = models.ForeignKey(Cliente, null=True)
    agente = models.ForeignKey(Agente, null=True)
    tipoSeguro = models.ForeignKey(TipoSeguro, null=True)
    comparativa = models.ForeignKey(Comparativa, null=True)
    poliza = models.ForeignKey(Poliza, null=True)
    def __unicode__ (self):
        return "Orden de Servicio: " + self.idServicio + " Cliente: " + self.cliente + " Agente: " + self.agente;
