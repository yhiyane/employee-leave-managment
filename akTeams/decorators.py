from django.core.exceptions import PermissionDenied
from leaveManagementApp.models import Employee

def role_requiredadmin():


    def decorator(func):

        def wrap(request,*args,**kwargs):
            if request.user.is_superuser :
                return func(request,*args,**kwargs)
            else:
                raise PermissionDenied

        return wrap
    return decorator

def role_manager():


    def decorator(func):

        def wrap(request,*args,**kwargs):
            currentUser = Employee.objects.get(user=request.user)
            if currentUser.isManager :
                return func(request,*args,**kwargs)
            else:
                raise PermissionDenied

        return wrap
    return decorator