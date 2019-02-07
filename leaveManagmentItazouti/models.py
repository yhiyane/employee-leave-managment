from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Team(models.Model):
    team_code = models.CharField(max_length=10, null=True, blank=True, unique=True)
    libelle = models.CharField(max_length=200)

    def __str__(self):  # __unicode__ on Python 2
        return self.libelle


class Position(models.Model):
    position_code = models.CharField(max_length=10, null=True, blank=True, unique=True)
    libelle = models.CharField(max_length=200)

    def __str__(self):  # __unicode__ on Python 2
        return self.position_code


class BusinessEntity(models.Model):
    be_Code = models.CharField(max_length=10, null=True, blank=True, unique=True)
    libelle = models.CharField(max_length=200)

    def __str__(self):  # __unicode__ on Python 2
        return self.be_Code


class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    cin_code = models.CharField(max_length=10, unique=True)
    birth_date = models.DateField()
    hire_date = models.DateField()
    email = models.EmailField(max_length=100, blank=False, unique=True)
    cnss_code = models.CharField(max_length=30, unique=True)
    experience_years_number = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    leave_days_number = models.FloatField()
    resignation_date = models.DateField(null=True, blank=True)
    isManager = models.BooleanField(default=False)
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    be = models.ForeignKey(BusinessEntity, on_delete=models.SET_NULL, null=True)
    positon = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)
    team = models.ManyToManyField(Team)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.first_name


class LeaveType(models.Model):
    LeaveTypeCode = models.CharField(max_length=10, null=True, blank=True, unique=True)
    libelle = models.CharField(max_length=200)
    daysNumber = models.BigIntegerField(null=True, blank=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.libelle


def enum(*args):
    enums = dict(zip(args, range(len(args))))
    return type('Enum', (), enums)


STATUS = (('ACCEPTED', 'accepted'),
          ('REJECTED', 'rejected'),
          ('WAITING', 'waiting'),
          ('CANCELED', 'canceled')
          )


class LeaveRequest(models.Model):
    leave_request_code = models.CharField(max_length=10, null=True, blank=True, unique=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    create_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS,null=True, blank=True, max_length=50)
    reason = models.CharField(max_length=200)
    employee = models.ForeignKey(Employee, related_name='Employee', on_delete=models.SET_NULL, null=True)
    manager = models.ForeignKey(Employee, related_name='Manager', on_delete=models.SET_NULL, null=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.leave_request_code


class Leave(models.Model):
    leave_code = models.CharField(max_length=10, null=True, blank=True, unique=True)
    leave_date = models.DateTimeField()
    expected_return_date = models.DateTimeField()
    reason_leave = models.CharField(max_length=200)
    leave_request = models.ForeignKey(LeaveRequest, on_delete=models.SET_NULL, null=True)
    leave_type = models.ForeignKey(LeaveType, on_delete=models.SET_NULL, null=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.leave_code
