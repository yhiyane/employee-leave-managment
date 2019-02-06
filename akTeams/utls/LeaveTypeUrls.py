from django.urls import path

from akTeams.view import leaveTypeView



# map urls with views
urlpatterns = [
    #  leave Type
    path('', leaveTypeView.index, name='leaveType.index'),
    path('create', leaveTypeView.create, name='leaveType.create'),
    path('update/<int:id>', leaveTypeView.update, name='leaveType.update'),
    path('delete/<int:id>', leaveTypeView.delete, name='leaveType.delete'),




]