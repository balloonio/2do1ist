from django.test import TestCase, Client

# Create your tests here.
class UrlTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_details(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/accounts/logout/')
        self.assertEqual(response.status_code, 200)