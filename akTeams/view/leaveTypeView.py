from django.shortcuts import render,get_object_or_404,redirect
from leaveManagementApp.models import LeaveType
from akTeams.form.LeaveTypeForms import LeaveTypeForm
from django.contrib import messages
from akTeams.decorators import role_requiredadmin,role_manager
from django.contrib.auth.decorators import login_required
from akTeams.api.serializers import *
from django.http import JsonResponse

@login_required
@role_requiredadmin()
def index(request):
    list_leaveType = LeaveType.objects.all()
    context = {
        'list_leaveType': list_leaveType,
    }
    return render(request, 'leaveType/index.html', context)
#
@login_required
@role_requiredadmin()
def create(request):
    form = LeaveTypeForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Leave Type created')
        return redirect('leaveType.index')

    context = {
        'form': form,
        'modeCreate': True
    }

    return render(request, 'leaveType/formLeaveType.html', context)
# #
@login_required
@role_requiredadmin()
def update(request, id):

    item = get_object_or_404(LeaveType, pk=id)
    form = LeaveTypeForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        messages.info(request, 'Leave Type updated')
        return redirect('leaveType.index')


    context = {
        'form': form,
        'modeCreate': False
    }
    return render(request, 'leaveType/formLeaveType.html', context)
#
@login_required
@role_requiredadmin()
def delete(request, id):
        item = get_object_or_404(LeaveType, pk=id)
        item.delete()
        messages.error(request, 'Leave Type deleted')
        return redirect('leaveType.index')

def testRestFunction(request):

   if request.method == 'GET':

       list_leaveType = LeaveType.objects.all()
       serializer = LeaveTypeSerializer(list_leaveType,many=True)

       return JsonResponse(serializer.data,safe=False)