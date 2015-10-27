# -*- coding: utf-8 -*-
from selenium import webdriver
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import LiveServerTestCase
import os
import unittest
from ...models import Agente, ClienteFisico, ClienteMoral, Cliente
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import time

class NuevoClienteTest(LiveServerTestCase):
    def setUp(self):
        chromedriver = os.path.join(os.path.dirname(__file__), '../chromedriver/chromedriver.exe')
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.browser = webdriver.Chrome(chromedriver)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    def create_agente(self):
        user = User.objects.create_user(username='ivanalejandro', password='ivan',
        email='ivanali@outlook.com', first_name='Ivan', last_name='Soto')
        user.save()

        agente = Agente.objects.create(userAgente=user, claveAgente=12345)
        agente.save()

    def test_nuevo_cliente(self):
        self.create_agente()
        self.browser.get(self.get_full_url("schema:login"))
        self.browser.find_element_by_name("user").send_keys('ivanalejandro')
        self.browser.find_element_by_class_name("password").send_keys('ivan')
        self.browser.find_element_by_class_name("login").click()

        self.browser.find_element_by_id("clientes").click()
        self.browser.find_element_by_id("nuevoCliente").click()

        self.browser.find_element_by_name("nombre").send_keys('Ivan Alejandro')
        self.browser.find_element_by_name("apellidoPaterno").send_keys('Soto')
        self.browser.find_element_by_name("apellidoMaterno").send_keys('Velazquez')
        self.browser.find_element_by_name("edad").send_keys("20")
        self.browser.find_element_by_id("optionsRadios1").click()
        self.browser.find_element_by_name("email").send_keys('ivanali@outlook.com')
        self.browser.find_element_by_name("telefonoLada").send_keys('644')
        self.browser.find_element_by_name("telefono").send_keys('1421909')
        self.browser.find_element_by_name("rfc").send_keys('QWERTY')

        self.browser.find_element_by_name("crear").click()

        time.sleep(5)
        self.assertIn("Clientes", self.browser.title)
        # self.assertIn(row[1], "Ivan Alejandro")
