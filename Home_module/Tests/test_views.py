from django.test import SimpleTestCase
from django.urls import reverse, resolve

from ..views import HomeView

class TestHomeView(SimpleTestCase):
    def test_home_view(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, HomeView)