from schema.models import Agente
from django.contrib.auth.models import User

def create_agente():
    user = User.objects.create_user(username='ivanalejandro', password='ivan',
    email='ivanali@outlook.com', first_name='Ivan', last_name='Soto')
    user.save()

    agente = Agente.objects.create(userAgente=user, claveAgente=12345)
    agente.save()

def run():
    create_agente()
