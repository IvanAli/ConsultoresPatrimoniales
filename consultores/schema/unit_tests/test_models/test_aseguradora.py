# Create your tests here.
# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from schema.models import Aseguradora, TipoSeguro, Cobertura, DatoTipoSeguro, DatoCobertura

class TestAseguradora(TestCase):
    def test_create_seguro_add_to_aseguradora(self):

        # create the datos for tiposeguro
        dts1 = DatoTipoSeguro(llave='producto', valor='Autos individual')
        dts2 = DatoTipoSeguro(llave='plan', valor='Amplia VIP')
        dts3 = DatoTipoSeguro(llave='renovacion', valor='No')
        dts4 = DatoTipoSeguro(llave='formaPago', valor='Contado')
        dts5 = DatoTipoSeguro(llave='estadoCirculacion', valor='Guanajuato')
        dts6 = DatoTipoSeguro(llave='iva', valor='16')
        dts7 = DatoTipoSeguro(llave='vigencia', valor='Anual')
        dts8 = DatoTipoSeguro(llave='dias', valor='365')

        # save the datos
        dts1.save()
        dts2.save()
        dts3.save()
        dts4.save()
        dts5.save()
        dts6.save()
        dts7.save()
        dts8.save()

        # create the tiposeguro
        tipoSeguro = TipoSeguro(idTipoSeguro='AP')


        # create the datos for cobertura
        dc1 = DatoCobertura(llave='sumaAsegurada', valor='Valor Comercial')
        dc2 = DatoCobertura(llave='deducible', valor='5.00')
        dc3 = DatoCobertura(llave='primaNeta', valor='1,499.54')
        dc4 = DatoCobertura(llave='ampliaVip', valor='Si')
        dc5 = DatoCobertura(llave='ampliaUno', valor='Si')
        dc6 = DatoCobertura(llave='limitado', valor='No')

        # save the datos for cobertura
        dc1.save()
        dc2.save()
        dc3.save()
        dc4.save()
        dc5.save()
        dc6.save()

        # create the cobertura
        c = Cobertura(nombreCobertura='Danos materiales')

        # create the aseguradora
        aseguradora = Aseguradora(nombre='GNP Seguros', sitioWeb='www.gnp.com.mx', telefonoLada='123',
        telefono='1234567', calle='Somewhere', numeroExt=666, colonia='Over the rainbow', ciudad='Leon',
        estado='Guanajuato', codigoPostal='54321')

        # save the aseguradora
        aseguradora.save()

        # save the tiposeguro
        tipoSeguro.save()
        ### tipoSeguro.save()

        # add the datos to tiposeguro
        tipoSeguro.datos.add(dts1, dts2, dts3, dts4, dts5, dts6, dts7, dts8)

        # add the tipo seguro to the _set
        aseguradora.tiposeguro_set.add(tipoSeguro)

        # save the cobertura
        c.save()

        # add the datos to the cobertura
        c.datos.add(dc1, dc2, dc3, dc4, dc5, dc6)

        # add to the set of the tipo seguro
        tipoSeguro.cobertura_set.add(c)


        atmp = Aseguradora.objects.get(sitioWeb='www.gnp.com.mx')
        asegurotmp = atmp.tiposeguro_set.get(idTipoSeguro='AP')
        asegurodatotmp = asegurotmp.datos.get(llave='producto')

        
        self.assertIn(asegurodatotmp.valor, 'Autos individual')
