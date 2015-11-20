from schema.models import Aseguradora, Contacto
from django.contrib.auth.models import User

def create_contacto():
	contacto = Contacto(
		nombre='Juancho',
		apellidoPaterno='Pistolas',
		apellidoMaterno='de la Rosa',
		email='juan@gmail.com',
		telefonoLada='666',
		telefono='4564564',
		aseguradora=Aseguradora.objects.get(pk=1)
		)
	contacto.save()

def run():
	create_contacto()