# Create your tests here.
# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from schema.models import Aseguradora, TipoSeguro, Cobertura


# import EAV attributes module
"""
import eav
from eav.models import Attribute
from ...eav_config import TipoSeguroEavConfig, CoberturaEavConfig
"""

class TestAseguradora(TestCase):
    def test_hola(self):
        self.assertEqual(True, True)
