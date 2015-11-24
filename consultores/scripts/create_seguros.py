#SI
from schema.models import Seguro

def create_seguro():
    seguro = Seguro(idSeguro='AP', nombre='Automóviles y pickups')
    seguro.save()
    seguro = Seguro(idSeguro='C', nombre='Camiones')
    seguro.save()
    seguro = Seguro(idSeguro='R', nombre='Remolques, cajas secas y adaptaciones en general')
    seguro.save()
    seguro = Seguro(idSeguro='G', nombre='Gastos médicos mayores')
    seguro.save()
    seguro = Seguro(idSeguro='V', nombre='Vida')
    seguro.save()
    seguro = Seguro(idSeguro='H', nombre='Hogares')
    seguro.save()
    seguro = Seguro(idSeguro='I', nombre='Inversiones')
    seguro.save()
    seguro = Seguro(idSeguro='E', nombre='Empresas')
    seguro.save()
    seguro = Seguro(idSeguro='EC', nombre='Equipo de contratistas')
    seguro.save()
    seguro = Seguro(idSeguro='T', nombre='Transportes')
    seguro.save()

def delete_seguro():
    Seguro.objects.all().delete()

def run():
    delete_seguro()
    create_seguro()
