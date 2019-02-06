from leaveManagementApp.models import *
from .serializers import *
from rest_framework import viewsets

#ModeleViewSet regroupe :a set of views (ensemble des views ci dessus )
# all : list , create , delete , update , retrieve, partial-update

class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class BusinessEntityViewSet(viewsets.ModelViewSet):
    queryset = BusinessEntity.objects.all()
    serializer_class = BusinessEntitySerializer

class LeaveTypeViewSet(viewsets.ModelViewSet):
    queryset = LeaveType.objects.all()
    serializer_class = LeaveTypeSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

