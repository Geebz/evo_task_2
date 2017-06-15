from django.test import TestCase
from django.test.client import Client

from .models import Person
from .views import get_three_random_names


# Create your tests here.
class TestWinnersFunctionality(TestCase):
    def setUp(self):
        self.client = Client()

    def test_add_new_name(self):
        POST_DATA = {
            "name": "Саша"
        }

        self.client.post('/add_person/', data=POST_DATA, HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEqual(Person.objects.all().count(), 1)
        self.assertEqual(Person.objects.all()[0].name, 'Саша')

    def test_add_format_name(self):
        POST_DATA = {
            "name": "аЛекСандр"
        }

        self.client.post('/add_person/', data=POST_DATA, HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEqual(Person.objects.all().count(), 1)
        self.assertEqual(Person.objects.all()[0].name, 'Александр')

    def test_the_same_one_name(self):
        POST_DATA = {
            "name": "Саша"
        }

        self.client.post('/add_person/', data=POST_DATA, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.client.post('/add_person/', data=POST_DATA, HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEqual(Person.objects.all().count(), 1)

    def test_add_more_names(self):
        POST_DATA = {
            "name": "Саша"
        }

        self.client.post('/add_person/', data=POST_DATA, HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        POST_DATA.update({"name": "Петя"})
        self.client.post('/add_person/', data=POST_DATA, HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEqual(Person.objects.all().count(), 2)

    def test_delete_existing_name(self):
        Person.objects.create(name='Саша')

        POST_DATA = {
            "name": "Саша"
        }

        self.client.post('/delete_person/', data=POST_DATA, HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEqual(Person.objects.all().count(), 0)

    def test_delete_not_existing_name(self):

        POST_DATA = {
            "name": "Саша"
        }

        self.client.post('/delete_person/', data=POST_DATA, HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEqual(Person.objects.all().count(), 0)

    def test_delete_existing_name_another_format(self):
        Person.objects.create(name='Саша')

        POST_DATA = {
            "name": "СаША"
        }

        self.client.post('/delete_person/', data=POST_DATA, HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEqual(Person.objects.all().count(), 0)

    def test_random_names_less_than_three(self):
        Person.objects.create(name='Саша')
        Person.objects.create(name='Оля')

        res = get_three_random_names()

        self.assertEqual(len(res), 2)
        self.assertTrue('Саша' in res)
        self.assertTrue('Оля' in res)

    def test_random_names_exactly_three(self):
        Person.objects.create(name='Саша')
        Person.objects.create(name='Оля')
        Person.objects.create(name='Вася')

        res = get_three_random_names()

        self.assertEqual(len(res), 3)
        self.assertTrue('Саша' in res)
        self.assertTrue('Оля' in res)
        self.assertTrue('Вася' in res)

    def test_random_names_more_than_three(self):
        Person.objects.create(name='Саша')
        Person.objects.create(name='Оля')
        Person.objects.create(name='Вася')
        Person.objects.create(name='Валик')

        res = get_three_random_names()

        self.assertEqual(len(res), 3)