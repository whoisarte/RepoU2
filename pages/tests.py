from django.test import SimpleTestCase
from django.urls import reverse

class SimpleTestCase(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_whoami_page_status_code(self):
        response = self.client.get(reverse("whoami"))
        self.assertEqual(response.status_code, 200)


