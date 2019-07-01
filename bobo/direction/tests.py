from django.test import TestCase
from django.urls import reverse


class Test(TestCase):
    
    def test_map_page(self):
        response = self.client.get(reverse('map'))
        self.assertEqual(response.status_code, 200)


    def test_navebarre_page(self):
        response = self.client.get(reverse('navebarre_vent'))
        self.assertEqual(response.status_code, 200)

