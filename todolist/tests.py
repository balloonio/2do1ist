from django.test import TestCase
import requests

# Create your tests here.
# PythonAnywhere deactivates the project website every few months:
#
# "We're happy to host your free website -- and keep it free -- for as long as you want to keep it running, 
# but you'll need to log in at least once every three months and click the "Run until 3 months from today" button below. 
# We'll send you an email a week before the site is disabled so that you don't forget to do that." - PythonAnywhere
#
# Adding this test to capure the website inactivity status, so that I can re-activate the website asap.

class PythonAnywhereTestCase(TestCase):
    def setUp(self):
        self.URL = "https://2do.pythonanywhere.com"
        self.DEACTIVATED_STATUS_CODE = 404

    def test_url_is_not_deactivated(self):
        response_status_code = requests.get(url=self.URL).status_code
        self.assertNotEqual(response_status_code, self.DEACTIVATED_STATUS_CODE)
