from django.db import models

### REVISAR IMPLEMENTACION DE URL PARA CADA CLASE
    #def get_absolute_url(self):
    #    from django.core.urlresolvers import reverse
    #    return reverse()

### REVISAR BLANK=TRUE Y NULL=TRUE
    # ¿Cada vez que un campo no sea obligatorio (blank=True), hay que ponerle null=True también?

### REVISAR META DATOS DE CADA MODELO
    # Se pone Meta en cada uno?

# Create your models here.
class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=30)
    contrasena = models.CharField(max_length=30)
    nombre = models.CharField(max_length=40)
    apellidoPaterno = models.CharField(max_length=30)
    apellidoMaterno = models.CharField(max_length=30)
    edad = models.PositiveSmallIntegerField()
    SEXO_OPCIONES = (
        ('M', 'Mujer'),
        ('H', 'Hombre'),
        ('O', 'Otro'),
        )
    sexo = models.CharField(max_length=1, choices=SEXO_OPCIONES)
    rfc = models.CharField(max_length=13)
    email = models.EmailField(max_length=254)
    telefonoLada = models.CharField(max_length=3)
    telefono = models.CharField(max_length=7)
    calle = models.CharField(max_length=50, blank=True)
    numeroExt = models.PositiveSmallIntegerField(blank=True)
    numeroInt = models.PositiveSmallIntegerField(blank=True)
    colonia = models.CharField(max_length=40, blank=True)
    ciudad = models.CharField(max_length=30, blank=True)
    estado = models.CharField(max_length=19, blank=True)
    codigoPostal = models.CharField(max_length=5, blank=True)
    class Meta:
        abstract = True
    def __unicode__(self):
        return "Usuario: " + self.nombre +" "+ self.apellidoPaterno +" "+ self.apellidoMaterno

class Cliente(Usuario):
    linkRegistroRFC = models.URLField(null=True)
    linkComprobanteDomicilio = models.URLField(null=True)
    calleFact = models.CharField(max_length=50)
    numeroExtFact = models.PositiveSmallIntegerField()
    numeroIntFact = models.PositiveSmallIntegerField(blank=True)
    coloniaFact = models.CharField(max_length=40)
    ciudadFact = models.CharField(max_length=30)
    estadoFact = models.CharField(max_length=19)
    codigoPostalFact = models.CharField(max_length=5)
    def __unicode__(self):
        return "Cliente: " + self.nombre +" "+ self.apellidoPaterno +" "+ self.apellidoMaterno

class ClienteFisico(Cliente):
    def __unicode__(self):
        return "Persona Física: " + self.nombre +" "+ self.apellidoPaterno +" "+ self.apellidoMaterno

class ClienteMoral(Cliente):
    razonSocial = models.CharField(max_length=100)
    linkActaConstitutiva = models.URLField()
    linkIdRepresentante = models.URLField()
    def __unicode__(self):
        return "Persona Moral: " + self.nombre +" "+ self.apellidoPaterno +" "+ self.apellidoMaterno

class Agente(Usuario):
    claveAgente = models.IntegerField(blank=True, null=True)
    cuentaBancaria = models.CharField(max_length=34)
    banco = models.CharField(max_length=30)
    def __unicode__(self):
        return "Agente: " + self.nombre +" "+ self.apellidoPaterno +" "+ self.apellidoMaterno

class OrdenServicio(models.Model):
    idServicio = models.AutoField(primary_key=True)
    fechaServicio = models.DateTimeField(auto_now_add=True, 'fecha de servicio')
    fechaConclusion = models.DateTimeField(blank=True, null=True)
    cliente = models.ForeignKey(Cliente)
    agente = models.ForeignKey(Agente)
    tipoSeguro = models.ForeignKey(TipoSeguro)
    comparativa = models.ForeignKey(Comparativa)
    poliza = models.ForeignKey(Poliza)
    def __unicode__ (self):
        return "Orden de Servicio: " + self.idServicio + " Cliente: " + self.cliente + " Agente: " + self.agente;

class Comparativa(models.Model):
    idComparativa = models.AutoField(primary_key=True)
    numeroCotizaciones = models.PositiveIntegerField()
    fechaCreacion = models.DateTimeField(auto_now_add=True, 'fecha creada')
    fechaConclusion = models.DateTimeField(blank=True, null=True, 'fecha concluida')
    fechaEnvio = models.DateTimeField(blank=True, null=True, 'fecha de envio')
    cliente = models.ForeignKey(Cliente)
    agente = models.ForeignKey(Agente)
    def __unicode__(self):
        return "Comparativa: " + self.idComparativa + " Cliente: " + self.cliente + " Agente: " + self.agente

class CoberturasRequeridas(models.model):
    comparativa = models.ForeignKey(Comparativa)
    cobertura = models.ForeignKey(Cobertura)
    def __unicode__(self):
        return "Cobertura " + self.cobertura + " requerida en Comparativa " + self.comparativa

class CoberturasUtilizadas(models.model):
    poliza = models.ForeignKey(Poliza)
    cobertura = models.ForeignKey(Cobertura)
    def __unicode__(self):
        return "Cobertura " + self.cobertura + " utilizada en Poliza " + self.poliza

class Cotizacion(models.Model):
    idCotizacion = models.AutoField(primary_key=True)
    costo = models.DecimalField(max_digits=11, decimal_places=2)
    fechaCreacion = models.DateTimeField('fecha creada')
    FORMA_PAGO_OPCIONES = (
        (12, 'Anual'),
        (6, 'Semestral'),
        (3, 'Trimestral'),
    )
    formaPago = models.IntegerField(choices=FORMA_PAGO_OPCIONES, default=12)
    comparativa = models.ForeignKey(Comparativa)
    aseguradora = models.ForeignKey(Aseguradora)
    def __unicode__(self):
        return "Cotizacion: " + self.idCotizacion + " de comparativa: " + self.comparativa

class Poliza(models.Model):
    idPoliza = models.AutoField(primary_key=True)
    primaNeta = models.DecimalField(max_digits=11, decimal_places=2)
    fechaEmision = models.DateTimeField('fecha emitida')
    fechaInicio = models.DateTimeField('fecha de inicio')
    fechaFin = models.DateTimeField('fecha de fin')
    endosoBeneficiario = models.CharField(max_length=50)
    linkCaratulaPDF = models.URLField(max_length=200)
    cliente = models.ForeignKey(Cliente)
    agente = models.ForeignKey(Agente)
    comision = models.ForeignKey(Comision)
    aseguradora = models.ForeignKey(Aseguradora)
    def __unicode__(self):
        return "Póliza: " + self.idPoliza + "Cliente: " + self.cliente + "Agente: " + self.agente

class Pago(models.Model):
    idPago = models.AutoField(primary_key=True)
    cantidad = models.DecimalField(max_digits=11, decimal_places=2)
    fechaPago = models.DateTimeField('fecha de pago')
    numeroPago = models.PositiveSmallIntegerField()
    poliza = models.ForeignKey(Poliza)
    def __unicode__(self):
        return "Pago " + self.numeroPago + " de Poliza " + self.poliza

class Comision(models.Model):
    idComision = models.AutoField(primary_key=True)
    cantidadComision = models.DecimalField(max_digits=11, decimal_places=2)
    fechaDeposito = models.DateTimeField(null=True)
    asignacionComision = models.ForeignKey(AsignacionComision)
    agente = models.ForeignKey(Agente)
    def __unicode__(self):
        return "Comisión " + self.idComision + " de Agente " + self.agente

class AsignacionComision(models.Model):
    idAsignacion = models.AutoField(primary_key=True)
    fechaAsignacion = models.DateTimeField('fecha de asignacion')
    porcentaje = models.DecimalField(max_digits=4, decimal_places=2)
    tipoSeguro = models.ForeignKey(TipoSeguro)
    aseguradora = models.ForeignKey(Aseguradora)
    def __unicode__(self):
        return "Asignacion de Comisión: " + self.idAsignacion + " Tipo de Seguro: " + self.tipoSeguro + " Aseguradora: " + self.aseguradora

class Contacto(models.Model):
# Should it inherit from Persona?
# Response: I don't think so, it is independant to our system
    idContacto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellidoPaterno = models.CharField(max_length=30)
    apellidoMaterno = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    telefonoLada = models.CharField(max_length=3, blank=True)
    telefono = models.CharField(max_length=7, blank=True)
    aseguradora = models.ForeignKey(Aseguradora)
    def __unicode__(self):
        return "Contacto: " + self.idContacto + " Aseguradora: " + self.aseguradora

class Aseguradora(models.Model):
    idAseguradora = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    sitioWeb = models.URLField(blank=True)
    telefonoLada = models.CharField(max_length=3)
    telefono = models.CharField(max_length=7)
    ### Estos campos son opcionales? 
    calle = models.CharField(max_length=50, blank=True)
    numeroExt = models.PositiveSmallIntegerField(blank=True)
    numeroInt = models.PositiveSmallIntegerField(blank=True)
    colonia = models.CharField(max_length=40, blank=True)
    ciudad = models.CharField(max_length=30, blank=True)
    estado = models.CharField(max_length=19, blank=True)
    codigoPostal = models.CharField(max_length=5, blank=True)
    def __unicode__(self):
        return "Aseguradora: " + self.nombre

class TipoSeguro(models.Model):
    ### No será mejor poner el ID como las iniciales de SEGUROS_OPCIONES?
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
    def __unicode__(self):
        return "Seguro: " + self.tipoSeguro

class SegurosOfertados(models.Model):
    aseguradora = models.ForeignKey(Aseguradora)
    seguro = models.ForeignKey(TipoSeguro)
    def __unicode__(self):
        return "Aseguradora " + self.aseguradora + " oferta Seguro " + self.seguro

class Dato(models.Model):
    idDato = models.AutoField(primary_key=True)
    nombreDato = models.CharField(max_length=50)
    ### Está bien modelado esto? No estoy seguro cómo modelarlo, lo comentamos el lunes
    tipoDato = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)
    def __unicode__(self):
        return "Dato: " + self.nombreDato + " Tipo: " + self.tipoDato

class DatosNecesitados(models.Model):
    seguro = models.ForeignKey(TipoSeguro)
    dato = models.ForeignKey(Dato)
    def __unicode__(self):
        return "Dato " + self.dato + " es necesario en Seguro " + self.seguro

class Cobertura(models.Model):
    idCobertura = models.AutoField(primary_key=True)
    nombreCobertura = models.CharField(max_length=50)
    descripcion = models.TextField()
    porcentajeCobertura = models.DecimalField(max_digits=4, decimal_places=2)
    seguro = models.ForeignKey(TipoSeguro)
    def __unicode__(self):
        return "Cobertura: " + self.nombreCobertura + " pertenece a Seguro: " + self.seguro