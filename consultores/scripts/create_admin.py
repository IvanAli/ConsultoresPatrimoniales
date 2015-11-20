#SI
from schema.models import Administrador
from django.contrib.auth.models import User

def create_admin():
    user = User.objects.create_user(username='joaquintech', password='joaquin',
    email='joaquin_tech@hotmail.com', first_name='Joaquin', last_name='Gutierrez')
    user.save()

    admin = Administrador.objects.create(userAdmin=user)
    admin.save()

def run():
    create_admin()