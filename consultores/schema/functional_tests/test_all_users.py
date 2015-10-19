# -*- coding: utf-8 -*-
from selenium import webdriver
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import LiveServerTestCase
import os
import unittest


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        # chromedriver = "C:/Users/Ivan/Consultores/consultores/functional_tests/chromedriver/chromedriver.exe"
        chromedriver = os.path.join(os.path.dirname(__file__), 'chromedriver/chromedriver.exe')
        os.environ["webdriver.chrome.driver"] = chromedriver
        # driver = webdriver.Chrome(chromedriver)
        self.browser = webdriver.Chrome(chromedriver)
        # driver = webdriver.Chrome()
        # self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    """
    def test_it_worked(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Welcome to Django', self.browser.title)
    """
    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    def test_home_title(self):
        self.browser.get(self.get_full_url("schema:home"))
        self.assertIn("Consultores Patrimoniales", self.browser.title)

    def test_h1_css(self):
        self.browser.get(self.get_full_url("schema:home"))
        h1 = self.browser.find_element_by_tag_name("h1")
        self.assertEqual(h1.value_of_css_property("color"), "rgba(200, 50, 255, 1)")
