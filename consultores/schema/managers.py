# User manager

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UsuarioManager(BaseUserManager):
    def create_user(self, usuario, password, nombre, apellidoPaterno, apellidoMaterno, email):
        user = self.model(usuario=usuario, contrasena=password, nombre=nombre, apellidoPaterno=apellidoPaterno,
        apellidoMaterno=apellidoMaterno, email=email)
        return user

    def create_superuser(self, usuario, password, nombre, apellidoPaterno, apellidoMaterno, email):
        user = self.create_user(usuario, password, nombre, apellidoPaterno, apellidoMaterno, email)
        user.save()
        return user
