from django.test import TestCase,Client
from django.urls import resolve,reverse
from akTeams.views import index,update
from leaveManagementApp.models import Team
import  json

class testViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('team.index')
    def test_index(self):

        response = self.client.get(self.list_url)
        print(response)
        self.assertEquals(response.status_code, 302)
        # self.assertTemplateUsed(response,'akTeams/team/index.html')

#
#     def test_update(self):
#         url = reverse('team.update',args=[1])
#         self.assertEquals(resolve(url).func, update)