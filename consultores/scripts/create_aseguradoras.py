#SI
from schema.models import Aseguradora

def create_aseguradoras():
    aseguradora = Aseguradora(nombre='GNP Seguros', sitioWeb='http://www.gnp.com.mx', telefonoLada=442, telefono=1234567, calle='Rainbow', numeroExt=1234, colonia='asdf', ciudad='Queretaro', estado='Queretaro', codigoPostal=54321)
    aseguradora.save()

    aseguradora = Aseguradora(nombre='Seguros Potosi', sitioWeb='http://www.segurospotosi.com.mx', telefonoLada=442, telefono=1234567, calle='Rainbow', numeroExt=1234, colonia='asdf', ciudad='Queretaro', estado='Queretaro', codigoPostal=54321)
    aseguradora.save()

    aseguradora = Aseguradora(nombre='MAPFRE', sitioWeb='http://www.mapfre.com.mx', telefonoLada=442, telefono=1234567, calle='Rainbow', numeroExt=1234, colonia='asdf', ciudad='Queretaro', estado='Queretaro', codigoPostal=54321)
    aseguradora.save()

    aseguradora = Aseguradora(nombre='AXA', sitioWeb='https://axa.mx/', telefonoLada=442, telefono=1234567, calle='Rainbow', numeroExt=1234, colonia='asdf', ciudad='Queretaro', estado='Queretaro', codigoPostal=54321)
    aseguradora.save()

    aseguradora = Aseguradora(nombre='AXA', sitioWeb='https://axa.mx/', telefonoLada=442, telefono=1234567, calle='Rainbow', numeroExt=1234, colonia='asdf', ciudad='Queretaro', estado='Queretaro', codigoPostal=54321)
    aseguradora.save()

    aseguradora = Aseguradora(nombre='Zurich', sitioWeb='https://www.zurich.com.mx/es-mx/', telefonoLada=442, telefono=1234567, calle='Rainbow', numeroExt=1234, colonia='asdf', ciudad='Queretaro', estado='Queretaro', codigoPostal=54321)
    aseguradora.save()

def run():
    create_aseguradoras()
