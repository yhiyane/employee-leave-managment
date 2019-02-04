from django.contrib import admin
from .models import Employee, Team, BusinessUnit, Position, Profile

# Register your models here.
admin.site.register(Employee)
admin.site.register(Team)
admin.site.register(Position)
admin.site.register(BusinessUnit)
admin.site.register(Profile)

