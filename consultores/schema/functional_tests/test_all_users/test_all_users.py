# -*- coding: utf-8 -*-
from selenium import webdriver
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import LiveServerTestCase
import os
import unittest
from ...models import Agente
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import time

class AgentLoginTest(LiveServerTestCase):
    def setUp(self):
        chromedriver = os.path.join(os.path.dirname(__file__), '../chromedriver/chromedriver.exe')
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.browser = webdriver.Chrome(chromedriver)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    def test_user_authentication(self):
        user = User.objects.create_user(username='ivanalejandro', password='ivan',
        email='ivanali@outlook.com', first_name='Ivan', last_name='Soto')
        user.save()

        agente = Agente.objects.create(userAgente=user, claveAgente=12345)
        agente.save()

        self.browser.get(self.get_full_url("schema:login"))
        self.browser.find_element_by_name("user").send_keys('ivanalejandro')
        self.browser.find_element_by_class_name("password").send_keys('ivan')
        self.browser.find_element_by_class_name("login").click()

        time.sleep(5)

        self.assertIn("Consultores Patrimoniales", self.browser.title)

    """
    def test_agent_authentication_no_pass(self):
        agente = Agente(usuario='')
        agente = Agente(usuario="IvanAli1", contrasena="ivan", nombre="Ivan Alejandro", apellidoPaterno="Soto",
        apellidoMaterno="Velazquez", edad=20, sexo="M", rfc="SOVI", email="ivanali@outlook.com",
        telefonoLada="644", telefono="1421909", calle="Jesús Oviedo", numeroExt=106, numeroInt=33,
        colonia="Villas del Tecnológico", ciudad="Santiago de Querétaro", estado="Querétaro", codigoPostal="76150",
        claveAgente=12345, cuentaBancaria="abcdefg", banco="Santander")
        agente.save()

        self.browser.get(self.get_full_url("schema:login"))
        inputAgent = self.browser.find_element_by_name("user")
        inputPass = self.browser.find_element_by_name("password")
        loginButton = self.browser.find_element_by_name("login")

        inputAgent.send_keys(agente.usuario)

        loginButton.click()
        self.assertIn("Log in", self.browser.title)

    def test_agent_authentication_all_fields(self):
        agente = Agente(usuario="IvanAli", contrasena="ivan", nombre="Ivan Alejandro", apellidoPaterno="Soto",
        apellidoMaterno="Velazquez", edad=20, sexo="M", rfc="SOVI", email="ivanali@outlook.com",
        telefonoLada="644", telefono="1421909", calle="Jesús Oviedo", numeroExt=106, numeroInt=33,
        colonia="Villas del Tecnológico", ciudad="Santiago de Querétaro", estado="Querétaro", codigoPostal="76150",
        claveAgente=12345, cuentaBancaria="abcdefg", banco="Santander")
        agente.save()

        self.browser.get(self.get_full_url("schema:login"))
        inputAgent = self.browser.find_element_by_name("user")
        inputPass = self.browser.find_element_by_name("password")
        loginButton = self.browser.find_element_by_name("login")

        inputAgent.send_keys(agente.usuario)
        inputPass.send_keys(agente.contrasena)

        loginButton.click()
        self.assertIn("Consultores Patrimoniales", self.browser.title)
    """
"""
class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        # chromedriver = "C:/Users/Ivan/Consultores/consultores/functional_tests/chromedriver/chromedriver.exe"
        chromedriver = os.path.join(os.path.dirname(__file__), '../chromedriver/chromedriver.exe')
        os.environ["webdriver.chrome.driver"] = chromedriver
        # driver = webdriver.Chrome(chromedriver)
        self.browser = webdriver.Chrome(chromedriver)
        # driver = webdriver.Chrome()
        # self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    def test_login_title(self):
        self.browser.get(self.get_full_url("schema:login"))
        self.assertIn("Log in", self.browser.title)


    def test_robot_human_files(self):
        self.browser.get(self.live_server_url + "/robots.txt")
        self.assertNotIn("Not Found", self.browser.title)
        self.browser.get(self.live_server_url + "/humans.txt")
        self.assertNotIn("Not Found", self.browser.title)
"""
