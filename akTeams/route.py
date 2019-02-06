from akTeams.api.viewsets import *
from django.urls import  path
from rest_framework import routers
from akTeams.view.leaveTypeView import  testRestFunction

route = routers.DefaultRouter()
route.register('position', PositionViewSet)
route.register('bu', BusinessEntityViewSet)
route.register('leaveType', LeaveTypeViewSet)
route.register('team', TeamViewSet)
route.register('employee', EmployeeViewSet)

# urlpatterns = [
#
#     path('leaveType/',testRestFunction),
#     ]
