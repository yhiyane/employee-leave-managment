# Create your models here.
from django.db import models
from django.utils import timezone
from datetime import date,time
from django.contrib.auth.models import User

# Create your models here.





class BusinessEntity(models.Model):
    be_Code = models.CharField(max_length=10, null=True, blank=True, unique=True)
    libelle = models.CharField(max_length=200)

    def __str__(self):  # __unicode__ on Python 2
        return self.libelle

class Position(models.Model):
    position_code = models.CharField(max_length=10, null=True, blank=True, unique=True)
    libelle = models.CharField(max_length=200)

    def __str__(self):  # __unicode__ on Python 2
        return self.libelle

class LeaveType(models.Model):
    LeaveTypeCode = models.CharField(max_length=10, null=True, blank=True, unique=True)
    libelle = models.CharField(max_length=200)
    daysNumber = models.IntegerField(default=0)

    def __str__(self):  # __unicode__ on Python 2
        return self.libelle

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
    leave_days_number = models.FloatField(default=0)
    resignation_date = models.DateField
    be = models.ForeignKey(BusinessEntity, on_delete=models.SET_NULL, null=True)  # business unit
    positon = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)  # business unit
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    isManager = models.BooleanField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):  # __unicode__ on Python 2
        return self.first_name + ' '+ self.last_name


class Team(models.Model):
    team_code = models.CharField(max_length=10, null=True, blank=True, unique=True)
    libelle = models.CharField(max_length=200)
    members = models.ManyToManyField(Employee)

    def __str__(self):  # __unicode__ on Python 2
        return self.libelle


# class MemberTeam(models.Model):
#     employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
#     team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
#     date_affectation = models.DateField
#     affectation_reason = models.CharField(max_length=200)

MYSTATUS = (
   ('Waiting', 'WAITING'),
   ('Rejected', 'REJECTED'),
   ('Accepted', 'ACCEPTED'),
   ('Canceled', 'CANCELED'),
)


class LeaveRequest(models.Model):
    # leave_request_code = models.CharField(max_length=10, null=True, blank=True, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    debutHeure = models.TimeField()
    finHeure = models.TimeField()
    create_date = models.DateTimeField(auto_now=True, blank=True)
    status = models.CharField(max_length=10, choices=MYSTATUS)
    reason = models.TextField(null=True)
    leave_type = models.ForeignKey(LeaveType, on_delete=models.SET_NULL, null=True)
    employee = models.ForeignKey(Employee, related_name='Employee', on_delete=models.SET_NULL, null=True)
    isVu = models.BooleanField(default=False)
    # manager = models.ForeignKey(Employee, related_name='Manager', on_delete=models.SET_NULL, null=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.employee


class Leave(models.Model):
    leave_code = models.CharField(max_length=10, null=True, blank=True, unique=True)
    leave_date = models.DateTimeField
    expected_return_date = models.DateTimeField
    reason_leave = models.TextField
    leave_request = models.ForeignKey(LeaveRequest, on_delete=models.SET_NULL, null=True)
    leave_type = models.ForeignKey(LeaveType, on_delete=models.SET_NULL, null=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.leave_code