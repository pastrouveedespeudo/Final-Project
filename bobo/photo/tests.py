from django.test import TestCase
from django.urls import reverse


class Test(TestCase):
    
    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


    def test_coupe(self):
        response = self.client.get(reverse('coupe'))
        self.assertEqual(response.status_code, 200)


    def test_navebarre_coupe(self):
        response = self.client.get(reverse('navebarre_coupe'))
        self.assertEqual(response.status_code, 200)


    def test_habits(self):
        response = self.client.get(reverse('habits'))
        self.assertEqual(response.status_code, 200)

    def test_navebarre_habits(self):
        response = self.client.get(reverse('navebarre_habits'))
        self.assertEqual(response.status_code, 200)


    def test_tendance(self):
        response = self.client.get(reverse('tendance'))
        self.assertEqual(response.status_code, 200)


    def test_navebarre_admin2(self):
        response = self.client.get(reverse('navebarre_admin2'))
        self.assertEqual(response.status_code, 200)


    def test_database_mode(self):
        response = self.client.get(reverse('database_mode'))
        self.assertEqual(response.status_code, 200)













        
