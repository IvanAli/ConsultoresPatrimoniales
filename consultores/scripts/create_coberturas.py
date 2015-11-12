from schema import models

def create_coberturas_AP():
    cobertura = models.Cobertura(nombre='Danos materiales', tipo='AP')
    cobertura.save()
    cobertura = models.Cobertura(nombre='Exencion de deducible por perdida total', tipo='AP')
    cobertura.save()
    cobertura = models.Cobertura(nombre='Deducible cero en robo total', tipo='AP')
    cobertura.save()
    cobertura = models.Cobertura(nombre='Responsabilidad civil danos a bienes y personas', tipo='AP')
    cobertura.save()
    cobertura = models.Cobertura(nombre='Robo parcial', tipo='AP')
    cobertura.save()
    cobertura = models.Cobertura(nombre='Gastos medicos ocupantes', tipo='AP')
    cobertura.save()

def create_coberturas_C():
    cobertura = models.Cobertura(nombre='Danos materiales', tipo='C')
    cobertura.save()
    cobertura = models.Cobertura(nombre='Exencion de deducible por perdida total', tipo='C')
    cobertura.save()
    cobertura = models.Cobertura(nombre='Deducible cero en robo total', tipo='C')
    cobertura.save()
    cobertura = models.Cobertura(nombre='Responsabilidad civil danos a bienes y personas', tipo='C')
    cobertura.save()
    cobertura = models.Cobertura(nombre='Robo parcial', tipo='C')
    cobertura.save()
    cobertura = models.Cobertura(nombre='Gastos medicos ocupantes', tipo='C')
    cobertura.save()

def create_coberturas_G():
    cobertura = models.Cobertura(nombre='Emergencias en el extranjero', tipo='G')
    cobertura.save()
    cobertura = models.Cobertura(nombre='Cobertura en el extranjero', tipo='G')
    cobertura.save()
    cobertura = models.Cobertura(nombre='Continuacion familiar', tipo='G')
    cobertura.save()

def create_coberturas_E():
    cobertura = models.Cobertura(nombre='Incendio/rayo', tipo='E')
    cobertura.save()
    cobertura = models.Cobertura(nombre='Huracan', tipo='E')
    cobertura.save()
    cobertura = models.Cobertura(nombre='Extension de cubierta', tipo='E')
    cobertura.save()
    cobertura = models.Cobertura(nombre='Terremoto', tipo='E')
    cobertura.save()
    cobertura = models.Cobertura(nombre='Explosion', tipo='E')
    cobertura.save()
    cobertura = models.Cobertura(nombre='Objetos caidos de aviones', tipo='E')
    cobertura.save()
    cobertura = models.Cobertura(nombre='Huelgas y alborotos populares', tipo='E')
    cobertura.save()

def run():
    create_coberturas_AP()
    create_coberturas_C()
    create_coberturas_G()
    create_coberturas_E()
