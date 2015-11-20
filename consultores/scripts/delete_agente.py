#SI
from schema.models import Agente
from django.contrib.auth.models import User

def run():
    User.objects.all().delete()
    Agente.objects.all().delete()
