#NECESITA REVISION
from schema.models import Comparativa, Cotizacion, TipoSeguro, SeguroAP, 

def run():
    Cotizacion.objects.all().delete()
    Comparativa.objects.all().delete()
    TipoSeguro.objects.all().delete()
