#SI
from schema.models import Cobertura, Seguro

def create_coberturas_AP():
    cobertura = Cobertura(nombre='Daños materiales', seguro=Seguro.objects.get(pk='AP'))
    cobertura.save()
    cobertura = Cobertura(nombre='Exención de deducible por perdida total', seguro=Seguro.objects.get(pk='AP'))
    cobertura.save()
    cobertura = Cobertura(nombre='Deducible cero en robo total', seguro=Seguro.objects.get(pk='AP'))
    cobertura.save()
    cobertura = Cobertura(nombre='Responsabilidad civil daños a bienes y personas', seguro=Seguro.objects.get(pk='AP'))
    cobertura.save()
    cobertura = Cobertura(nombre='Robo parcial', seguro=Seguro.objects.get(pk='AP'))
    cobertura.save()
    cobertura = Cobertura(nombre='Gastos médicos ocupantes', seguro=Seguro.objects.get(pk='AP'))
    cobertura.save()

def create_coberturas_C():
    cobertura = Cobertura(nombre='Daños materiales', seguro=Seguro.objects.get(pk='C'))
    cobertura.save()
    cobertura = Cobertura(nombre='Exención de deducible por pérdida total', seguro=Seguro.objects.get(pk='C'))
    cobertura.save()
    cobertura = Cobertura(nombre='Deducible cero en robo total', seguro=Seguro.objects.get(pk='C'))
    cobertura.save()
    cobertura = Cobertura(nombre='Responsabilidad civil de daños a bienes y personas', seguro=Seguro.objects.get(pk='C'))
    cobertura.save()
    cobertura = Cobertura(nombre='Robo parcial', seguro=Seguro.objects.get(pk='C'))
    cobertura.save()
    cobertura = Cobertura(nombre='Gastos médicos de ocupantes', seguro=Seguro.objects.get(pk='C'))
    cobertura.save()

def create_coberturas_G():
    cobertura = Cobertura(nombre='Emergencias en el extranjero', seguro=Seguro.objects.get(pk='G'))
    cobertura.save()
    cobertura = Cobertura(nombre='Cobertura en el extranjero', seguro=Seguro.objects.get(pk='G'))
    cobertura.save()
    cobertura = Cobertura(nombre='Continuación familiar', seguro=Seguro.objects.get(pk='G'))
    cobertura.save()

def create_coberturas_E():
    cobertura = Cobertura(nombre='Incendio/rayo', seguro=Seguro.objects.get(pk='E'))
    cobertura.save()
    cobertura = Cobertura(nombre='Huracán', seguro=Seguro.objects.get(pk='E'))
    cobertura.save()
    cobertura = Cobertura(nombre='Extensión de cubierta', seguro=Seguro.objects.get(pk='E'))
    cobertura.save()
    cobertura = Cobertura(nombre='Terremoto', seguro=Seguro.objects.get(pk='E'))
    cobertura.save()
    cobertura = Cobertura(nombre='Explosión', seguro=Seguro.objects.get(pk='E'))
    cobertura.save()
    cobertura = Cobertura(nombre='Objetos caídos de aviones', seguro=Seguro.objects.get(pk='E'))
    cobertura.save()
    cobertura = Cobertura(nombre='Huelgas y alborotos populares', seguro=Seguro.objects.get(pk='E'))
    cobertura.save()

def create_coberturas_I():
    cobertura = Cobertura(nombre='Inversión inteligente', seguro=Seguro.objects.get(pk='I'))
    cobertura.save()

def run():
    Cobertura.objects.all().delete()
    create_coberturas_AP()
    create_coberturas_C()
    create_coberturas_G()
    create_coberturas_E()
