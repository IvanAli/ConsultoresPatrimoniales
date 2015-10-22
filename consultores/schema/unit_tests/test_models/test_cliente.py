# auto-header: generate
# Testeo para crear un cliente
from django.test import TestCase
from schema.models import ClienteFisico, Cliente, ClienteMoral

class TestCliente(TestCase):
    def test_client_fisico_not_all_fields(self):
        clientefis = ClienteFisico(nombre="Ivan Alejandro", apellidoPaterno="Soto",
        apellidoMaterno="Velazquez", edad=20, sexo="M", rfc="SOVI", email="ivanali@outlook.com",
        telefonoLada="644", telefono="1421909", calle="Jesús Oviedo", numeroExt=106, numeroInt=33,
        colonia="Villas del Tecnológico", ciudad="Santiago de Querétaro", estado="Querétaro",
        codigoPostal="76150", calleFact="Jesus Oviedo", numeroExtFact=106, numeroIntFact=103,
        coloniaFact="Villas del Tecnologico", ciudadFact="Queretaro", estadoFact="Queretaro")

        clientefis.save()
        self.assertEqual(clientefis, ClienteFisico.objects.get(pk=clientefis.pk))
