from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Employee)
admin.site.register(Team)
admin.site.register(Position)
admin.site.register(BusinessEntity)
admin.site.register(LeaveType)
admin.site.register(LeaveRequest)
admin.site.register(Leave)
