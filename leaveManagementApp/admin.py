from django.contrib import admin

from leaveManagementApp.models import Employee, LeaveRequest, Leave, Team, BusinessEntity, Position, LeaveType


# Register your models here.

admin.site.register(Employee)
admin.site.register(LeaveRequest)
admin.site.register(Leave)
admin.site.register(Team)
admin.site.register(BusinessEntity)
admin.site.register(Position)
admin.site.register(LeaveType)
#admin.site.register(MemberTeam)
