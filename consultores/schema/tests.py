# Testeo de la pagina home
# Author: Ivan
# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Agente

class TestHomePage(TestCase):
    def test_uses_index_template(self):
        response = self.client.get(reverse("schema:home"))
        self.assertTemplateUsed(response, "schema/index.html")

    def test_uses_base_template(self):
        response = self.client.get(reverse("schema:home"))
        self.assertTemplateUsed(response, "base.html")
