#NECESITA REVISION
from schema.models import Agente, Cliente, ClienteFisico, OrdenServicio, TipoSeguro, Aseguradora, Comparativa, Poliza, SeguroAP, CoberturaAP
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

def create_cliente():
    cf1 = ClienteFisico(nombre="Ivan Alejandro", apellidoPaterno="Soto",
    apellidoMaterno="Velazquez", edad=20, sexo="M", rfc="SOVI", email="ivanali@outlook.com",
    telefonoLada="644", telefono="1421909", calle="Jesús Oviedo", numeroExt=106, numeroInt=33,
    colonia="Villas del Tecnológico", ciudad="Santiago de Querétaro", estado="Querétaro",
    codigoPostal="76150", calleFact="Jesus Oviedo", numeroExtFact=106, numeroIntFact=103,
    coloniaFact="Villas del Tecnologico", ciudadFact="Queretaro", estadoFact="Queretaro")

    cf1.save()

def create_orden_servicio():
    orden = OrdenServicio(cliente=Cliente.objects.order_by('-pk')[0],
    	agente = Agente.objects.order_by('-pk')[0],
    	tipoSeguro=TipoSeguro.objects.order_by('-pk')[0])
    orden.save()

def create_poliza():
    poliza = Poliza(
    	primaNeta=987,
    	ordenServicio=OrdenServicio.objects.order_by('-pk')[0],
    	cotizacion = Cotizacion.objects.order_by('-pk')[0],
    	fechaEmision=timezone.now() - datetime.timedelta(days=10),
    	fechaInicio=timezone.now(),
    	fechaFin=fechaInicio + datetime.timedelta(days=365),
    	endosoBeneficiario="no se que va aqui")
    poliza.save()

def run():
	create_cliente()
	create_orden_servicio()
	create_poliza()