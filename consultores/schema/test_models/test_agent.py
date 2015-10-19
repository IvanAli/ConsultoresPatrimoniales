# Create your tests here.
# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Agente

class TestAgentRegistration(TestCase):
    def test_register_agent_all_fields(self):
        agente = Agente(usuario="Ivan", contrasena="ivan", nombre="Ivan Alejandro", apellidoPaterno="Soto",
        apellidoMaterno="Velazquez", edad=20, sexo="M", rfc="SOVI", email="ivanali@outlook.com",
        telefonoLada="644", telefono="1421909", calle="Jesús Oviedo", numeroExt=106, numeroInt=33,
        colonia="Villas del Tecnológico", ciudad="Santiago de Querétaro", estado="Querétaro", codigoPostal="76150",
        claveAgente=12345, cuentaBancaria="abcdefg", banco="Santander")

        agente.save()
        self.assertEqual(agente.idUsuario, Agente.objects.get(usuario="Ivan",contrasena="ivan").idUsuario)

    def test_register_agent_not_all_fields(self):
        agente = Agente(usuario="IvanAlejandro", contrasena="ivan", nombre="Ivan Alejandro", apellidoPaterno="Soto",
        apellidoMaterno="Velazquez", edad=20, sexo="M", rfc="SOVI", email="ivanali@outlook.com",
        telefonoLada="644", telefono="1421909", calle="Jesús Oviedo", numeroExt=106)

        agente.save()
        self.assertEqual(agente.idUsuario, Agente.objects.get(usuario="IvanAlejandro",contrasena="ivan").idUsuario)
        self.assertEqual(Agente.objects.get(usuario="IvanAlejandro").colonia, None)

    def test_user_password_required(self):
        agente = Agente(nombre="Ivan Alejandro", apellidoPaterno="Soto",
        apellidoMaterno="Velazquez", edad=20, sexo="M", rfc="SOVI", email="ivanali@outlook.com",
        telefonoLada="644", telefono="1421909", calle="Jesús Oviedo", numeroExt=106)

        agente.save()
        self.assertNotEqual(agente.usuario, None)
