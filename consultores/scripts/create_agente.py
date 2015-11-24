#SI
from schema.models import Agente
from django.contrib.auth.models import User

def create_agente():
    for i in range(0,100):
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

def delete_agentes():
    for agente in Agente.objects.all():
        agente.delete()
    for user in User.objects.all():
        user.delete()

def run():
    delete_agentes()
    create_agente()