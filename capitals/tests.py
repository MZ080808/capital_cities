from django.test import TestCase
from .models import Capital
from django.urls import reverse

# Create your tests here.


class CapitalTests(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "Capital Cities")

    def test_capital_creatview(self):
        response = self.client.post(
            reverse("capital_new"),
            {"city": "Washington DC", "country": "United States of America"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Capital.objects.last().city, "Washington DC")
        self.assertEqual(Capital.objects.last().country, "United States of America")

    @classmethod
    def setUpTestData(cls):
        cls.capital = Capital.objects.create(city="riga", country="latvia")

    def test_capital_city(self):
        self.assertEqual(self.capital.city, "riga")

    def test_capital_country(self):
        self.assertEqual(self.capital.country, "latvia")
