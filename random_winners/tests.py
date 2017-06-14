from django.test import TestCase
from django.test.client import Client

from .views import send_form
from .models import Person


# Create your tests here.
class TestAddPersons(TestCase):
    def setUp(self):
        self.client = Client()

    def test_add_new_name(self):
        POST_DATA = {
            "name": "Саша"
        }

        self.client.post('', data=POST_DATA)

        self.assertTrue(Person.objects.all().count(), 1)
        self.assertTrue(Person.objects.all()[0], 'Саша')

    def test_format_name(self):
        POST_DATA = {
            "name": "сАШа"
        }

        self.client.post('', data=POST_DATA)

        self.assertTrue(Person.objects.all().count(), 1)
        self.assertTrue(Person.objects.all()[0], 'Саша')

    def test_the_same_one_name(self):
        POST_DATA = {
            "name": "Саша"
        }

        self.client.post('', data=POST_DATA)
        self.client.post('', data=POST_DATA)

        self.assertTrue(Person.objects.all().count(), 1)

    def test_add_more_names(self):
        POST_DATA = {
            "name": "Саша"
        }

        self.client.post('', data=POST_DATA)

        POST_DATA.update({"name": "Петя"})
        self.client.post('', data=POST_DATA)

        self.assertTrue(Person.objects.all().count(), 2)
