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
    email = models.EmailField(max_length=254)
    edad = models.PositiveSmallIntegerField(null=True)
    SEXO_OPCIONES = (
        ('M', 'Mujer'),
        ('H', 'Hombre'),
        )
    sexo = models.CharField(max_length=1, choices=SEXO_OPCIONES)
    rfc = models.CharField(max_length=13, blank=True)
    telefonoLada = models.PositiveSmallIntegerField(max_length=3)
    telefono = models.PositiveIntegerField(max_length=7)
    calle = models.CharField(max_length=50, blank=True)
    numeroExt = models.PositiveSmallIntegerField(blank=True, null=True)
    numeroInt = models.CharField(max_length=6,blank=True, null=True)
    colonia = models.CharField(max_length=40, blank=True)
    ciudad = models.CharField(max_length=30, blank=True)
    estado = models.CharField(max_length=19, blank=True)
    codigoPostal = models.PositiveSmallIntegerField(blank=True, null=True)
    class Meta:
        abstract = True
    def __str__(self):
        return "Persona"

class Cliente(Persona):
    idCliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellidoPaterno = models.CharField(max_length=30)
    apellidoMaterno = models.CharField(max_length=30)
    # Tal vez los siguientes campos deban ser obligatorios para cuando se ingresen
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

class Aseguradora(models.Model):
    idAseguradora = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    sitioWeb = models.URLField(blank=True, null=True)
    telefonoLada = models.CharField(max_length=3)
    telefono = models.CharField(max_length=7)
    calle = models.CharField(max_length=50, blank=True)
    numeroExt = models.PositiveSmallIntegerField(blank=True)
    numeroInt = models.PositiveSmallIntegerField(blank=True)
    colonia = models.CharField(max_length=40, blank=True)
    ciudad = models.CharField(max_length=30, blank=True)
    estado = models.CharField(max_length=19, blank=True)
    codigoPostal = models.CharField(max_length=5, blank=True)
    seguros = models.ManyToManyField('TipoSeguro', through='SegurosOfertados')

    def __str__(self):
        return "Aseguradora: " + self.nombre

# NECESARIO CHECAR .ptr Y COBERTURAS DE CADA SEGURO
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
    # idTipoSeguro = models.CharField(max_length=3, choices=SEGUROS_OPCIONES, primary_key=True)
    idTipoSeguro = models.AutoField(primary_key=True)

    def __str__(self):
    	return "Seguro: " + self.idTipoSeguro

class SegurosOfertados(models.Model):
    aseguradora = models.ForeignKey('Aseguradora')
    tipoSeguro = models.ForeignKey('TipoSeguro')

    class Meta:
        unique_together = ("aseguradora", "tipoSeguro")

    # def __str__(self):
    #     return self.aseguradora.nombre + " - " + self.tipoSeguro.idTipoSeguro

### DEPRECATED
# class DatoCobertura(models.Model):
#     llave = models.CharField(max_length=40, primary_key=True)
#     valor = models.CharField(max_length=80)
#     class Meta:
#         unique_together = ("llave", "valor")
#     def __str__(self):
#         return self.llave + ": " + self.valor

### DEPRECATED
# class Cobertura(models.Model):
#     """
#         Considerar que la Cobertura puede tambien tener muchos datos y la descripcion
#         puede que no sea suficiente

#         Se creo DatoCobertura para solucionar esto.
#     """

#     idCobertura = models.AutoField(primary_key=True)
#     nombreCobertura = models.CharField(max_length=50, null=True)
#     tipoSeguro = models.ForeignKey(TipoSeguro, null=True)
#     datos = models.ManyToManyField(DatoCobertura)

#     def __str__(self):
#         return "Cobertura: " + self.nombreCobertura

class Comparativa(models.Model):
    idComparativa = models.AutoField(primary_key=True)
    fechaCreacion = models.DateTimeField('fecha creada', auto_now_add=True)
    fechaConclusion = models.DateTimeField('fecha concluida', blank=True, null=True)
    fechaEnvio = models.DateTimeField('fecha de envio', blank=True, null=True)
    tipoSeguro = models.ForeignKey('TipoSeguro')
    # cliente = models.ForeignKey(Cliente, null=True)
    # agente = models.ForeignKey(Agente, null=True)

    def __str__(self):
        return "Comparativa: " + self.idComparativa + " Cliente: " + self.cliente + " Agente: " + self.agente

### HACE FALTA RESOLVER LO DE COBERTURAS
class Cotizacion(models.Model):
    idCotizacion = models.AutoField(primary_key=True)
    costo = models.DecimalField(max_digits=11, decimal_places=2)
    fechaCreacion = models.DateTimeField('fecha creada', auto_now_add=True)
    FORMA_PAGO_OPCIONES = (
        (12, 'Anual'),
        (6, 'Semestral'),
        (3, 'Trimestral'),
    )
    formaPago = models.IntegerField(choices=FORMA_PAGO_OPCIONES, default=12)
    comparativa = models.ForeignKey('Comparativa')
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
    # cliente = models.ForeignKey(Cliente, null=True)
    # agente = models.ForeignKey(Agente, null=True)
    comision = models.OneToOneField('Comision')
    # aseguradora = models.ForeignKey(Aseguradora, null=True)
    cotizacion = models.OneToOneField('Cotizacion')
    ordenServicio = models.OneToOneField('OrdenServicio')
    def __str__(self):
        return "Póliza: " + self.idPoliza + "Cliente: " + self.cliente + "Agente: " + self.agente

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

class SeguroAP(TipoSeguro):
    idSeguro = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=30, null=True, blank=True)
    modelo = models.CharField(max_length=30, blank=True, null=True)
    ano = models.PositiveSmallIntegerField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    pasajeros = models.PositiveSmallIntegerField(blank=True, null=True)
    estadoCirculacion = models.CharField(max_length=19, blank=True, null=True)

    def __str__(self):
        return "SeguroAP" + self.idSeguro

# NECESARIO RESOLVER ASUNTO DE COBERTURAS
class CoberturaAP(models.Model):
    idCobertura = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=41)
    sumaAsegurada = models.DecimalField(max_digits=11, decimal_places=11, blank=True, null=True)
    deducible = models.DecimalField(max_digits=11, decimal_places=11, blank=True, null=True)
    primaNeta = models.DecimalField(max_digits=11, decimal_places=11, blank=True, null=True)
    ampliaVip = models.NullBooleanField(blank=True)
    ampliaUno = models.NullBooleanField(blank=True)
    limitado = models.NullBooleanField(blank=True)
    seguroAP = models.ForeignKey('SeguroAP')



# class SeguroC(models.Model)
# class CoberturaC(models.Model)
# class SeguroR(models.Model)
# class CoberturaR(models.Model)
# class SeguroG(models.Model)
# class CoberturaG(models.Model)
# class SeguroV(models.Model)
# class CoberturaV(models.Model)
# class SeguroH(models.Model)
# class CoberturaH(models.Model)
# class SeguroI(models.Model)
# class CoberturaI(models.Model)
# class SeguroE(models.Model)
# class CoberturaE(models.Model)
# class SeguroEC(models.Model)
# class CoberturaEC(models.Model)
# class SeguroT(models.Model)
# class CoberturaT(models.Model)
# class SeguroESP(models.Model)
# class CoberturaESP(models.Model)
