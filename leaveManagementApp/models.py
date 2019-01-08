# Create your models here.
from django.db import models
from django.utils import timezone


# Create your models here.


# class STATUS(Enum):
#     ACCEPTED = 'accepted'
#     CANCELED = 'canceled'
#     REJECTED = 'rejected'
#     WAITING = 'waiting'

class Team(models.Model):
    team_code = models.CharField(max_length=10, null=True, blank=True, unique=True)
    libelle = models.CharField(max_length=200)


class BusinessEntity(models.Model):
    be_Code = models.CharField(max_length=10, null=True, blank=True, unique=True)
    libelle = models.CharField(max_length=200)


class Position(models.Model):
    position_code = models.CharField(max_length=10, null=True, blank=True, unique=True)
    libelle = models.CharField(max_length=200)


class LeaveType(models.Model):
    LeaveTypeCode = models.CharField(max_length=10, null=True, blank=True, unique=True)
    libelle = models.CharField(max_length=200)
    daysNumber = models.BigIntegerField


class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    cin_code = models.CharField(max_length=10, unique=True)
    birth_date = models.DateField()
    hire_date = models.DateField()
    email = models.EmailField(max_length=100, blank=False, unique=True)
    cnss_code = models.CharField(max_length=30, unique=True)
    experience_years_number = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    leave_days_number = models.FloatField
    resignation_date = models.DateField
    be = models.ForeignKey(BusinessEntity, on_delete=models.SET_NULL, null=True)  # business unit
    positon = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)  # business unit
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)


def enum(*args):
    enums = dict(zip(args, range(len(args))))
    return type('Enum', (), enums)


class LeaveRequest(models.Model):
    leave_request_code = models.CharField(max_length=10, null=True, blank=True, unique=True)
    start_date = models.DateTimeField
    end_date = models.DateTimeField
    create_date = models.DateTimeField
    status = enum('ACCEPTED', 'REJECTED', 'WAITING', 'CANCELED')
    reason = models.TextField
    employee = models.ForeignKey(Employee, related_name='Employee', on_delete=models.SET_NULL, null=True)
    manager = models.ForeignKey(Employee, related_name='Manager', on_delete=models.SET_NULL, null=True)


class Leave(models.Model):
    leave_code = models.CharField(max_length=10, null=True, blank=True, unique=True)
    leave_date = models.DateTimeField
    expected_return_date = models.DateTimeField
    reason_leave = models.TextField
    leave_request = models.ForeignKey(LeaveRequest, on_delete=models.SET_NULL, null=True)
    leave_type = models.ForeignKey(LeaveType, on_delete=models.SET_NULL, null=True)
