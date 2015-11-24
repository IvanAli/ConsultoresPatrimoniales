#SI
from schema.models import Agente, Aseguradora, Administrador, Seguro, Cobertura, Contacto, AreaTramites, Comision, AsignacionComision, ClienteAgente, Cliente
from django.contrib.auth.models import User

def create_agentes():
    for i in range(1,101):
        user = User.objects.create_user(
            username="user" + str(i),
            password=str(i),
            email='ivanali@outlook.com',
            first_name=str(i),
            last_name=str(i)+str(i),
            )
        user.save()

        agente = Agente.objects.create(
            userAgente=user,
            claveAgente=str(i*i),
            )
        agente.save()


    user = User.objects.create_user(
        username='ivanalejandro',
        password='ivan',
        email='ivanali@outlook.com',
        first_name='Ivan',
        last_name='Soto',
        )
    user.save()
    agente = Agente.objects.create(
        userAgente=user,
        claveAgente=12345,
        cuentaBancaria=999,
        banco='Santander',
        )
    agente.save()

    user = User.objects.create_user(
        username='squgus',
        password='gus',
        email='squgus@gmail.com',
        first_name='Gustavo',
        last_name='Gutierrez',
        )
    user.save()
    agente = Agente.objects.create(
        userAgente=user,
        claveAgente=666,
        cuentaBancaria=888,
        banco='Banamex',
        )
    agente.save()

    user = User.objects.create_user(
        username='gerardo',
        password='gera',
        email='gerchez93@gmail.com',
        first_name='Gerado',
        last_name='García',
        )
    user.save()
    agente = Agente.objects.create(
        userAgente=user,
        claveAgente=123456,
        cuentaBancaria=777,
        banco='Banorte',
        )
    agente.save()

def create_admin():
    user = User.objects.create_user(username='joaquintech', password='joaquin',
    email='joaquin_tech@hotmail.com', first_name='Joaquin', last_name='Gutierrez')
    user.save()

    admin = Administrador.objects.create(userAdmin=user)
    admin.save()

def create_clientes():
    for i in range(1,101):
        cliente = Cliente(
            email = str(i)+'mail@tumail.com',
            edad = i,
            sexo = 'M',
            telefonoLada = '666',
            telefono = '1234567',
            nombre = 'fulano' + str(i),
            apellidoPaterno = 'Pat' + str(i),
            apellidoMaterno = 'Mat' + str(i),
            calle = 'av' + str(i*i),
            numeroExt = str(i),
            numeroInt = i+i+i,
            colonia = 'col'+str(i+100),
            ciudad = 'Queretaro',
            estado = 'Queretaro',
            codigoPostal = str(i)+'1',
            )
        cliente.save()
        if i <= 50:
            CA = ClienteAgente(cliente=cliente, agente=Agente.objects.get(banco='Banamex'))
            CA.save()
        if i > 50:
            CA = ClienteAgente(cliente=cliente, agente=Agente.objects.get(banco='Banorte'))
            CA.save()


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

def create_contactos():
    for aseguradora in Aseguradora.objects.all():
        contacto = Contacto(
            nombre='Juancho',
            apellidoPaterno='Pistolas',
            apellidoMaterno='de la Rosa',
            email='juan@gmail.com',
            telefonoLada='666',
            telefono='4564564',
            aseguradora=aseguradora
            )
        contacto.save()
        contacto = Contacto(
            nombre='Juan',
            apellidoPaterno='Perez',
            apellidoMaterno='del Bosque',
            email='delbosque@gmail.com',
            telefonoLada='146',
            telefono='4564564',
            aseguradora=aseguradora
            )
        contacto.save()
        contacto = Contacto(
            nombre='Pedro',
            apellidoPaterno='Paramo',
            apellidoMaterno='Chancho',
            email='pedrero@gmail.com',
            telefonoLada='953',
            telefono='9876543',
            aseguradora=aseguradora
            )
        contacto.save()

def create_seguros():
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

def create_coberturas_AP():
    cobertura = Cobertura(nombre='Danos materiales', seguro=Seguro.objects.get(pk='AP'))
    cobertura.save()
    cobertura = Cobertura(nombre='Exencion de deducible por perdida total', seguro=Seguro.objects.get(pk='AP'))
    cobertura.save()
    cobertura = Cobertura(nombre='Deducible cero en robo total', seguro=Seguro.objects.get(pk='AP'))
    cobertura.save()
    cobertura = Cobertura(nombre='Responsabilidad civil danos a bienes y personas', seguro=Seguro.objects.get(pk='AP'))
    cobertura.save()
    cobertura = Cobertura(nombre='Robo parcial', seguro=Seguro.objects.get(pk='AP'))
    cobertura.save()
    cobertura = Cobertura(nombre='Gastos medicos ocupantes', seguro=Seguro.objects.get(pk='AP'))
    cobertura.save()

def create_coberturas_C():
    cobertura = Cobertura(nombre='Danos materiales', seguro=Seguro.objects.get(pk='C'))
    cobertura.save()
    cobertura = Cobertura(nombre='Exencion de deducible por perdida total', seguro=Seguro.objects.get(pk='C'))
    cobertura.save()
    cobertura = Cobertura(nombre='Deducible cero en robo total', seguro=Seguro.objects.get(pk='C'))
    cobertura.save()
    cobertura = Cobertura(nombre='Responsabilidad civil danos a bienes y personas', seguro=Seguro.objects.get(pk='C'))
    cobertura.save()
    cobertura = Cobertura(nombre='Robo parcial', seguro=Seguro.objects.get(pk='C'))
    cobertura.save()
    cobertura = Cobertura(nombre='Gastos medicos ocupantes', seguro=Seguro.objects.get(pk='C'))
    cobertura.save()

def create_coberturas_G():
    cobertura = Cobertura(nombre='Emergencias en el extranjero', seguro=Seguro.objects.get(pk='G'))
    cobertura.save()
    cobertura = Cobertura(nombre='Cobertura en el extranjero', seguro=Seguro.objects.get(pk='G'))
    cobertura.save()
    cobertura = Cobertura(nombre='Continuacion familiar', seguro=Seguro.objects.get(pk='G'))
    cobertura.save()

def create_coberturas_E():
    cobertura = Cobertura(nombre='Incendio/rayo', seguro=Seguro.objects.get(pk='E'))
    cobertura.save()
    cobertura = Cobertura(nombre='Huracan', seguro=Seguro.objects.get(pk='E'))
    cobertura.save()
    cobertura = Cobertura(nombre='Extension de cubierta', seguro=Seguro.objects.get(pk='E'))
    cobertura.save()
    cobertura = Cobertura(nombre='Terremoto', seguro=Seguro.objects.get(pk='E'))
    cobertura.save()
    cobertura = Cobertura(nombre='Explosion', seguro=Seguro.objects.get(pk='E'))
    cobertura.save()
    cobertura = Cobertura(nombre='Objetos caidos de aviones', seguro=Seguro.objects.get(pk='E'))
    cobertura.save()
    cobertura = Cobertura(nombre='Huelgas y alborotos populares', seguro=Seguro.objects.get(pk='E'))
    cobertura.save()

def create_coberturas_I():
    cobertura = Cobertura(nombre='Inversion inteligente', seguro=Seguro.objects.get(pk='I'))
    cobertura.save()

def create_area_tramites():
    AreaTramites.objects.all().delete()
    a = AreaTramites(encargado='Ivan Alejandro Soto Velazquez', email='ivanali@outlook.com')
    a.save()

def create_asignacion_comision():
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

def delete_users():
    Agente.objects.all().delete()
    Administrador.objects.all().delete()
    User.objects.all().delete()

def delete_aseguradoras():
    Aseguradora.objects.all().delete()

def delete_contactos():
    Contacto.objects.all().delete()

def delete_seguros():
    Seguro.objects.all().delete()

def delete_coberturas():
    Cobertura.objects.all().delete()

def delete_area_tramites():
    AreaTramites.objects.all().delete()

def delete_asignacion_comision():
    AsignacionComision.objects.all().delete()

def delete_clientes():
    ClienteAgente.objects.all().delete()
    Cliente.objects.all().delete

def run():
    delete_users()
    delete_aseguradoras()
    delete_contactos()
    delete_seguros()
    delete_coberturas()
    delete_clientes()

    create_admin()
    create_agentes()
    create_aseguradoras()
    create_contactos()
    create_seguros()
    create_coberturas_AP()
    create_coberturas_C()
    create_coberturas_G()
    create_coberturas_E()
    create_area_tramites()
    create_asignacion_comision()
    create_clientes()