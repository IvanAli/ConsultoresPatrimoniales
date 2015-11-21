#SI
from schema.models import Agente
from django.contrib.auth.models import User

def create_agente():
    user = User.objects.create_user(username='ivanalejandro', password='ivan',
    email='ivanali@outlook.com', first_name='Ivan', last_name='Soto')
    user.save()

    agente = Agente.objects.create(userAgente=user, claveAgente=12345, email=user.email, sexo='H',
    	telefonoLada=333, telefono=123456)
    agente.save()

    user = User.objects.create_user(username='squgus', password='gus',
    email='squgus@gmail.com', first_name='Gustavo', last_name='Gutierrez')
    user.save()

    agente = Agente.objects.create(userAgente=user, claveAgente=666, email=user.email, sexo='H',
        telefonoLada=666, telefono=6666666)
    agente.save()

def run():
    create_agente()
