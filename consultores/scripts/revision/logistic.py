#NECESITA REVISION
from schema.models import Agente, Cliente, ClienteFisico, OrdenServicio, TipoSeguro, Aseguradora, Comparativa, Poliza, SeguroAP, CoberturaAP
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

# whole logistic

def create_agente():
    user = User.objects.create_user(username='ivanalejandro', password='ivan',
    email='ivanali@outlook.com', first_name='Ivan', last_name='Soto')
    user.save()

    agente = Agente.objects.create(userAgente=user, claveAgente=12345)
    agente.save()

def create_cliente():
    cf1 = ClienteFisico(nombre="Ivan Alejandro", apellidoPaterno="Soto",
    apellidoMaterno="Velazquez", edad=20, sexo="M", rfc="SOVI", email="ivanali@outlook.com",
    telefonoLada="644", telefono="1421909", calle="Jesús Oviedo", numeroExt=106, numeroInt=33,
    colonia="Villas del Tecnológico", ciudad="Santiago de Querétaro", estado="Querétaro",
    codigoPostal="76150", calleFact="Jesus Oviedo", numeroExtFact=106, numeroIntFact=103,
    coloniaFact="Villas del Tecnologico", ciudadFact="Queretaro", estadoFact="Queretaro")

    cf1.save()

def create_tipoSeguro():
    seguroAP = TipoSeguro(tipo='AP')
    seguroAP.save()

    seguroC = TipoSeguro(tipo='C')
    seguroC.save()

    seguroR = TipoSeguro(tipo='R')
    seguroR.save()

    seguroG = TipoSeguro(tipo='G')
    seguroG.save()
# def create_tipo_seguro_aseguradora_datos():
#     # create Tipo de Seguro
#     seguroAP = TipoSeguro(idTipoSeguro='AP')

#     # create the aseguradora
#     aseguradora = Aseguradora(nombre='GNP Seguros', sitioWeb='www.gnp.com.mx', telefonoLada='123',
#     telefono='1234567', calle='Somewhere', numeroExt=666, colonia='Over the rainbow', ciudad='Leon',
#     estado='Guanajuato', codigoPostal='54321')

#     # create relacion between TipoSeguro & Aseguradora
#     S_A

#     ### Si no es abstracto Modelo Seguro, la siguiente línea es innecesaria
#     seguro = models.OneToOneField('TipoSeguro', default=0)
#     marca = models.CharField(max_length=30, blank=True, null=True)
#     modelo = models.CharField(max_length=30, blank=True, null=True)
#     ano = models.PositiveSmallIntegerField(blank=True, null=True)
#     descripcion = models.TextField(blank=True, null=True)
#     pasajeros = models.PositiveSmallIntegerField(blank=True, null=True)
#     estadoCirculacion = models.CharField(max_length=19, blank=True, null=True))

#     # save the datos


#     # create the tiposeguro
#     tipoSeguro = TipoSeguro(idTipoSeguro='AP')

#     # create the datos for cobertura
#     dc1 = DatoCobertura(llave='sumaAsegurada', valor='Valor Comercial')
#     dc2 = DatoCobertura(llave='deducible', valor='5.00')
#     dc3 = DatoCobertura(llave='primaNeta', valor='1,499.54')
#     dc4 = DatoCobertura(llave='ampliaVip', valor='Si')
#     dc5 = DatoCobertura(llave='ampliaUno', valor='Si')
#     dc6 = DatoCobertura(llave='limitado', valor='No')

#     # save the datos for cobertura
#     dc1.save()
#     dc2.save()
#     dc3.save()
#     dc4.save()
#     dc5.save()
#     dc6.save()

#     # create the cobertura
#     c = Cobertura(nombreCobertura='Danos materiales')



#     # save the aseguradora
#     aseguradora.save()

#     # save the tiposeguro
#     tipoSeguro.save()
#     ### tipoSeguro.save()

#     # add the datos to tiposeguro
#     tipoSeguro.datos.add(dts1, dts2, dts3, dts4, dts5, dts6, dts7, dts8)

#     # add the tipo seguro to the _set
#     aseguradora.tiposeguro_set.add(tipoSeguro)

#     # save the cobertura
#     c.save()

#     # add the datos to the cobertura
#     c.datos.add(dc1, dc2, dc3, dc4, dc5, dc6)

#     # add to the set of the tipo seguro
#     tipoSeguro.cobertura_set.add(c)

#     # spanglish rules


def create_orden_servicio():
    orden = OrdenServicio(cliente=Cliente.objects.order_by('-pk')[0],
    agente=Agente.objects.order_by('-pk')[0], tipoSeguro=TipoSeguro.objects.order_by('-pk')[0])
    orden.save()

def create_comparativa():
    comparativa = Comparativa(ordenServicio=OrdenServicio.objects.get(agente__userAgente__username='ivanalejandro',
    cliente__nombre='Ivan Alejandro'))
    comparativa.save()

def create_poliza():
    poliza = Poliza(primaNeta=987, ordenServicio=OrdenServicio.objects.get(agente__userAgente__username='ivanalejandro',
    cliente__nombre='Ivan Alejandro'), fechaFin=timezone.now() + datetime.timedelta(days=30), endosoBeneficiario="no se que va aqui")

    poliza.save()

def delete_all():
    User.objects.all().delete()
    Agente.objects.all().delete()
    TipoSeguro.objects.all().delete()
    Cliente.objects.all().delete()
    #Cobertura.objects.all().delete()
    OrdenServicio.objects.all().delete()
    Aseguradora.objects.all().delete()
    Comparativa.objects.all().delete()
    Poliza.objects.all().delete()

def run():
    delete_all()
    create_agente()
    # create_cliente()
    create_tipoSeguro()
    # create_orden_servicio()
    #create_tipo_seguro_aseguradora_datos()
    #create_orden_servicio()
    #create_comparativa()
    #create_poliza()
