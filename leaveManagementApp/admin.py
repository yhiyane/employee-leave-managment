from django.contrib import admin
from  django.contrib.auth import get_user_model
from leaveManagementApp.models import Employee, LeaveRequest, Leave, Team, BusinessEntity, Position, LeaveType

# Register your models here.
# User = get_user_model()
admin.site.register(Employee)
admin.site.register(LeaveRequest)
admin.site.register(Leave)
admin.site.register(Team)
admin.site.register(BusinessEntity)
admin.site.register(Position)
admin.site.register(LeaveType)
# admin.site.register(User)