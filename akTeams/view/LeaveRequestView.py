from django.shortcuts import render, get_object_or_404, redirect
from leaveManagementApp.models import MYSTATUS
from akTeams.form.leaveRequestForm import LeaveRequestForm
from leaveManagementApp.models import Employee, LeaveRequest
from django.contrib import messages
from datetime import date,time
from django.contrib.auth.decorators import login_required
from akTeams.decorators import role_requiredadmin,role_manager
from django.contrib.auth.decorators import login_required
@login_required
def index(request):
    currentUser = Employee.objects.get(user=request.user)


    list_reqLeave = LeaveRequest.objects.filter(employee=currentUser, create_date__year=date.today().year)
    context = {
        'list_reqLeave': list_reqLeave,
    }
    return render(request, 'LeaveRequest/index.html', context)
@login_required
def myleave(request, id):
    item = get_object_or_404(LeaveRequest, pk=id)
    if 'anuuler' in request.POST:
        print("Canceled")
        item.status = 'Canceled'
        item.save()
        messages.warning(request,str(item.employee ) + ' Leave request  Canceled')
        return redirect('leaveRqt.index')

    context = {
        'item': item,
    }
    return render(request, 'LeaveRequest/myleave.html', context)
@login_required
@role_manager()
def show(request, id):
    item = get_object_or_404(LeaveRequest, pk=id)
    if 'Accepted' in request.POST:
        print("accepted")
        item.status = 'Accepted'
        item.save()
        messages.success(request,str(item.employee ) + ' Leave request  Accepted')
        return redirect('leaveRqt.membres')

    elif 'Rejected' in request.POST:
        print("Rejected")
        item.status = 'Rejected'
        messages.error(request, str(item.employee ) + ' Leave request  Rejected')
        item.save()

        return redirect('leaveRqt.membres')

    context = {
        'item': item,
    }
    return render(request, 'LeaveRequest/show.html', context)

@login_required
@role_manager()
def getmembreLeaveReq(request):
    currentUser = Employee.objects.get(user=request.user)
    membres = Employee.objects.filter(manager=currentUser)

    membresLeaveRequests = LeaveRequest.objects. \
        filter(employee__in=membres, create_date__year=date.today().year,status='Waiting')


    context = {


        'membres_LeaveRequests': membresLeaveRequests,

    }
    return render(request, 'LeaveRequest/leaverequest.html', context)

@login_required
def create(request):
    currentUser = Employee.objects.get(user=request.user)
    # if 'Accepted' in request.POST:
    print(request.POST)
    form = LeaveRequestForm(request.POST or None)
    if form.is_valid():
        reqLeave = form.save(commit=False)
        partieJour = request.POST.get('partieJour')
        jourentier = request.POST.get('isJournee')
        if  jourentier != 'Yes':
            if partieJour == 'AM':
                print(" matinee ")
                reqLeave.debutHeure = time(8,30)
                reqLeave.finHeure = time(12,30)
                reqLeave.end_date = reqLeave.start_date
            else:
                print('apre midi')
                reqLeave.debutHeure = time(14, 0)
                reqLeave.finHeure = time(18, 0)
                reqLeave.end_date = reqLeave.start_date
        else:
            print('journee entier')
            reqLeave.debutHeure = time(8, 30)
            reqLeave.finHeure = time(18, 00)


        # print(request.POST.get('partieJour'))
        # print(request.POST.get('isJournee'))
        # print(form.cleaned_data)

        reqLeave.employee = currentUser
        reqLeave.status = 'Waiting'
        print(reqLeave.debutHeure)
        print(reqLeave.finHeure)
        reqLeave.save()
        messages.success(request, 'Leave Request created')
        return redirect('leaveRqt.index')

    context = {
        'form': form,
    }

    return render(request, 'LeaveRequest/formLeaverequest.html', context)


#
@login_required
def extraInfoUser(request):

    currentUser = Employee.objects.get(user=request.user)
    membres = Employee.objects.filter(manager=currentUser)

    membresLeaveRequests = LeaveRequest.objects.\
        filter(employee__in=membres,create_date__year=date.today().year,status='Waiting')
    ownerLeaveRequests = LeaveRequest.objects. \
        filter(employee=currentUser, create_date__year=date.today().year). \
        exclude(status__in=['Waiting', 'Canceled'])
    ismanager = currentUser.isManager
    # print(membresLeaveRequests)

    context = {
        'count': ownerLeaveRequests.count()+membresLeaveRequests.count(),
        'leaveRequests': ownerLeaveRequests,
        'membresLeaveRequests':membresLeaveRequests,
        'ismanager':ismanager,

    }
    return context
# @login_required
# def extraInfoUser(request):
#
#     currentUser = Employee.objects.get(user=request.user)
#     membres = Employee.objects.filter(manager=currentUser)
#
#     membresLeaveRequests = LeaveRequest.objects.\
#         filter(employee__in=membres,create_date__year=date.today().year,status='Waiting')
#     ownerLeaveRequests = LeaveRequest.objects. \
#         filter(employee=currentUser, create_date__year=date.today().year). \
#         exclude(status__in=['Waiting', 'Canceled'])
#
#     # print(membresLeaveRequests)
#
#     context = {
#         'count': ownerLeaveRequests.count()+membresLeaveRequests.count(),
#         'leaveRequests': ownerLeaveRequests,
#         'membresLeaveRequests':membresLeaveRequests,
#
#     }
#     return context