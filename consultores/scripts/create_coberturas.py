#SI
from schema import models

def create_coberturas_AP():
    cobertura = models.Cobertura(nombre='Danos materiales', seguro=models.Seguro.objects.get(pk='AP'))
    cobertura.save()
    cobertura = models.Cobertura(nombre='Exencion de deducible por perdida total', seguro=models.Seguro.objects.get(pk='AP'))
    cobertura.save()
    cobertura = models.Cobertura(nombre='Deducible cero en robo total', seguro=models.Seguro.objects.get(pk='AP'))
    cobertura.save()
    cobertura = models.Cobertura(nombre='Responsabilidad civil danos a bienes y personas', seguro=models.Seguro.objects.get(pk='AP'))
    cobertura.save()
    cobertura = models.Cobertura(nombre='Robo parcial', seguro=models.Seguro.objects.get(pk='AP'))
    cobertura.save()
    cobertura = models.Cobertura(nombre='Gastos medicos ocupantes', seguro=models.Seguro.objects.get(pk='AP'))
    cobertura.save()

def create_coberturas_C():
    cobertura = models.Cobertura(nombre='Danos materiales', seguro=models.Seguro.objects.get(pk='C'))
    cobertura.save()
    cobertura = models.Cobertura(nombre='Exencion de deducible por perdida total', seguro=models.Seguro.objects.get(pk='C'))
    cobertura.save()
    cobertura = models.Cobertura(nombre='Deducible cero en robo total', seguro=models.Seguro.objects.get(pk='C'))
    cobertura.save()
    cobertura = models.Cobertura(nombre='Responsabilidad civil danos a bienes y personas', seguro=models.Seguro.objects.get(pk='C'))
    cobertura.save()
    cobertura = models.Cobertura(nombre='Robo parcial', seguro=models.Seguro.objects.get(pk='C'))
    cobertura.save()
    cobertura = models.Cobertura(nombre='Gastos medicos ocupantes', seguro=models.Seguro.objects.get(pk='C'))
    cobertura.save()

def create_coberturas_G():
    cobertura = models.Cobertura(nombre='Emergencias en el extranjero', seguro=models.Seguro.objects.get(pk='G'))
    cobertura.save()
    cobertura = models.Cobertura(nombre='Cobertura en el extranjero', seguro=models.Seguro.objects.get(pk='G'))
    cobertura.save()
    cobertura = models.Cobertura(nombre='Continuacion familiar', seguro=models.Seguro.objects.get(pk='G'))
    cobertura.save()

def create_coberturas_E():
    cobertura = models.Cobertura(nombre='Incendio/rayo', seguro=models.Seguro.objects.get(pk='E'))
    cobertura.save()
    cobertura = models.Cobertura(nombre='Huracan', seguro=models.Seguro.objects.get(pk='E'))
    cobertura.save()
    cobertura = models.Cobertura(nombre='Extension de cubierta', seguro=models.Seguro.objects.get(pk='E'))
    cobertura.save()
    cobertura = models.Cobertura(nombre='Terremoto', seguro=models.Seguro.objects.get(pk='E'))
    cobertura.save()
    cobertura = models.Cobertura(nombre='Explosion', seguro=models.Seguro.objects.get(pk='E'))
    cobertura.save()
    cobertura = models.Cobertura(nombre='Objetos caidos de aviones', seguro=models.Seguro.objects.get(pk='E'))
    cobertura.save()
    cobertura = models.Cobertura(nombre='Huelgas y alborotos populares', seguro=models.Seguro.objects.get(pk='E'))
    cobertura.save()

def create_coberturas_I():
    cobertura = models.Cobertura(nombre='Inversion inteligente', seguro=models.Seguro.objects.get(pk='I'))
    cobertura.save()

def run():
    models.Cobertura.objects.all().delete()
    create_coberturas_AP()
    create_coberturas_C()
    create_coberturas_G()
    create_coberturas_E()
