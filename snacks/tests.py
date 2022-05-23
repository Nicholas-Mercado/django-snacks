from urllib import response
from django.test import SimpleTestCase
from django.urls import reverse

class SnackTests(SimpleTestCase):
    
    def test_home_status(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_about_status(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
