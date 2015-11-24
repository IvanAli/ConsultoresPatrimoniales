from schema.models import Seguro, Aseguradora, Comision, AsignacionComision

def create_asignacioncomision():
    gnp = Aseguradora.objects.get(nombre='GNP Seguros')
    mapfre = Aseguradora.objects.get(nombre='MAPFRE')
    potosi = Aseguradora.objects.get(nombre='Seguros Potosi')
    ac = AsignacionComision(porcentaje=5.00, seguro=Seguro.objects.get(pk='AP'), aseguradora=gnp)
    ac.save()
    ac = AsignacionComision(porcentaje=5.50, seguro=Seguro.objects.get(pk='AP'), aseguradora=mapfre)
    ac.save()
    ac = AsignacionComision(porcentaje=5.30, seguro=Seguro.objects.get(pk='AP'), aseguradora=potosi)
    ac.save()
    ac = AsignacionComision(porcentaje=5.00, seguro=Seguro.objects.get(pk='C'), aseguradora=gnp)
    ac.save()
    ac = AsignacionComision(porcentaje=5.50, seguro=Seguro.objects.get(pk='C'), aseguradora=mapfre)
    ac.save()
    ac = AsignacionComision(porcentaje=5.30, seguro=Seguro.objects.get(pk='C'), aseguradora=potosi)
    ac.save()
    ac = AsignacionComision(porcentaje=5.00, seguro=Seguro.objects.get(pk='R'), aseguradora=gnp)
    ac.save()
    ac = AsignacionComision(porcentaje=5.50, seguro=Seguro.objects.get(pk='R'), aseguradora=mapfre)
    ac.save()
    ac = AsignacionComision(porcentaje=5.30, seguro=Seguro.objects.get(pk='R'), aseguradora=potosi)
    ac.save()
    ac = AsignacionComision(porcentaje=5.00, seguro=Seguro.objects.get(pk='V'), aseguradora=gnp)
    ac.save()
    ac = AsignacionComision(porcentaje=5.50, seguro=Seguro.objects.get(pk='V'), aseguradora=mapfre)
    ac.save()
    ac = AsignacionComision(porcentaje=5.30, seguro=Seguro.objects.get(pk='V'), aseguradora=potosi)
    ac.save()
    ac = AsignacionComision(porcentaje=5.00, seguro=Seguro.objects.get(pk='G'), aseguradora=gnp)
    ac.save()
    ac = AsignacionComision(porcentaje=5.50, seguro=Seguro.objects.get(pk='G'), aseguradora=mapfre)
    ac.save()
    ac = AsignacionComision(porcentaje=5.30, seguro=Seguro.objects.get(pk='G'), aseguradora=potosi)
    ac.save()
    ac = AsignacionComision(porcentaje=5.00, seguro=Seguro.objects.get(pk='H'), aseguradora=gnp)
    ac.save()
    ac = AsignacionComision(porcentaje=5.50, seguro=Seguro.objects.get(pk='H'), aseguradora=mapfre)
    ac.save()
    ac = AsignacionComision(porcentaje=5.30, seguro=Seguro.objects.get(pk='H'), aseguradora=potosi)
    ac.save()
    ac = AsignacionComision(porcentaje=5.00, seguro=Seguro.objects.get(pk='I'), aseguradora=gnp)
    ac.save()
    ac = AsignacionComision(porcentaje=5.50, seguro=Seguro.objects.get(pk='I'), aseguradora=mapfre)
    ac.save()
    ac = AsignacionComision(porcentaje=5.30, seguro=Seguro.objects.get(pk='I'), aseguradora=potosi)
    ac.save()
    ac = AsignacionComision(porcentaje=5.00, seguro=Seguro.objects.get(pk='E'), aseguradora=gnp)
    ac.save()
    ac = AsignacionComision(porcentaje=5.50, seguro=Seguro.objects.get(pk='E'), aseguradora=mapfre)
    ac.save()
    ac = AsignacionComision(porcentaje=5.30, seguro=Seguro.objects.get(pk='E'), aseguradora=potosi)
    ac.save()
    ac = AsignacionComision(porcentaje=5.00, seguro=Seguro.objects.get(pk='EC'), aseguradora=gnp)
    ac.save()
    ac = AsignacionComision(porcentaje=5.50, seguro=Seguro.objects.get(pk='EC'), aseguradora=mapfre)
    ac.save()
    ac = AsignacionComision(porcentaje=5.30, seguro=Seguro.objects.get(pk='EC'), aseguradora=potosi)
    ac.save()
    ac = AsignacionComision(porcentaje=5.00, seguro=Seguro.objects.get(pk='T'), aseguradora=gnp)
    ac.save()
    ac = AsignacionComision(porcentaje=5.50, seguro=Seguro.objects.get(pk='T'), aseguradora=mapfre)
    ac.save()
    ac = AsignacionComision(porcentaje=5.30, seguro=Seguro.objects.get(pk='T'), aseguradora=potosi)
    ac.save()

def run():
    create_asignacioncomision()