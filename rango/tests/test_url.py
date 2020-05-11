






from django.test import SimpleTestCase
from django.url import reverse, resolve
from rango import views

class TestUrls(SimpleTestCase):

    def test_index_url(self):
        url = reverse("index")
        self.assertEquals(resolve(url).func, views.index)