from django.test import TestCase
from .models import Profile

class ProfileTestCase(TestCase):
    def setUp(self):
        self.ludo = Profile.objects.create(url="tinder.com/ludo")
        

    def test_url(self):
        self.assertEqual(self.ludo.url, "tinder.com/ludo")
        