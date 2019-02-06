from django.db.models.fields.related_descriptors import create_forward_many_to_many_manager
from rest_framework import  serializers
from leaveManagementApp.models import *


class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = ('id','position_code', 'libelle')

class BusinessEntitySerializer(serializers.ModelSerializer):

    class Meta:
        model = BusinessEntity
        fields = ('id','be_Code', 'libelle')

class LeaveTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = LeaveType
        fields = ('id','LeaveTypeCode', 'libelle','daysNumber')

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('__all__')
        # depth = 1

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    # members = EmployeeSerializer(many=True)
    class Meta:
        model = Team
        fields = ('id','team_code', 'libelle','members')

    # def create(self, validated_data):
    #     data = validated_data.pop('members')
    #     team = Team.objects.create(**validated_data)
    #     Employee.objects.create(**data)
    #     return team

