from django.db import models
from settingEmployer.models import Employee
from django.utils import timezone
import datetime

# Create your models here.

STATUS = (('ACCEPTED', 'accepted'),
          ('REJECTED', 'rejected'),
          ('WAITING', 'waiting'),
          ('CANCELED', 'canceled')
          )
MOTIF = (('Sick Day', 'Sick Day'),
         ('Unpaid', 'Unpaid'),
         ('Recovery', 'Recovery'),
         ('Vacation', 'Vacation'),
         ('Parental Leave', 'Parental Leave')
         )


class LeaveRequest(models.Model):
    leave_request_code = models.CharField(max_length=10, null=True, blank=True, unique=True)
    start_date = models.DateField(default=timezone.now)
    start_time = models.TimeField(default=datetime.time(8, 00, 00))
    end_date = models.DateField(default=timezone.now)
    end_time = models.TimeField(default=datetime.time(17, 00, 00))
    create_date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.CharField(choices=STATUS, null=True, blank=True, max_length=50)
    motif = models.CharField(choices=MOTIF, null=True, blank=True, max_length=50)
    reason = models.TextField(max_length=200, null=True, blank=True)
    employee = models.ForeignKey(Employee, related_name='Employee', on_delete=models.SET_NULL, blank=True, null=True)
    manager = models.ForeignKey(Employee, related_name='Manager', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.leave_request_code


class Notifications(models.Model):
    title = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(Employee, related_name='Created_By', on_delete=models.SET_NULL, blank=True,
                                   null=True)
    created_to = models.ForeignKey(Employee, related_name='Created_To', on_delete=models.SET_NULL, blank=True,
                                   null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tag_vu = models.BooleanField(default=False)
    leave_request = models.ForeignKey(LeaveRequest, related_name='Leave_Request', on_delete=models.SET_NULL, blank=True,
                                   null=True)

    def __str__(self):
        return self.title
