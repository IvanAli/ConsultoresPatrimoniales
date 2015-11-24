#SI
from schema.models import Administrador, Agente
from django.contrib.auth.models import User

def delete_users():
	Administrador.objects.all().delete()
	Agente.objects.all().delete()
	User.objects.all().delete()

def run():
	delete_users()