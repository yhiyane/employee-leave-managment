from django.urls import path

from akTeams.view import LeaveRequestView



# map urls with views
urlpatterns = [
    #  LeaveRequest
    path('', LeaveRequestView.index, name='leaveRqt.index'),
    path('create', LeaveRequestView.create, name='leaveRqt.create'),
    path('membres', LeaveRequestView.getmembreLeaveReq, name='leaveRqt.membres'),
    path('<int:id>', LeaveRequestView.show, name='leaveRqt.show'),
    path('myleave/<int:id>', LeaveRequestView.myleave, name='leaveRqt.showMyleave'),




]