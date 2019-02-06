from django.test import SimpleTestCase
from django.urls import resolve,reverse
from akTeams.views import index,update

class testUrls(SimpleTestCase):

    def test_list(self):
        url = reverse('team.index')
        self.assertEquals(resolve(url).func, index)

    def test_update(self):
        url = reverse('team.update',args=[1])
        self.assertEquals(resolve(url).func, update)