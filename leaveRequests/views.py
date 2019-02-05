from django.shortcuts import render, redirect, get_object_or_404
from .forms import LeaveRequestForm
from .models import Employee, LeaveRequest
from django.contrib import messages


# Create your views here.

def index_leave(request):
    if request.method == 'POST':
        user = request.user
        employer = Employee.objects.get(user_id=user.id)
        form = LeaveRequestForm(request.POST or None)
        try:
            manager = Employee.objects.get(id=employer.manager_id)
            if form.is_valid():
                leave_request = form.save(commit=False)
                leave_request.employee = employer
                leave_request.manager = manager
                leave_request.status = "waiting"
                leave_request.save()
                messages.success(request, 'You have sent the leave request to your manager successfully !!')
                return redirect('/leave/requestList')
            else:
                print(form.errors)
        except:
            print("this user haven't a manager yet .You  can't send this request!! ")
    else:
        form = LeaveRequestForm()
    context = {
        'form': form
    }
    return render(request, 'requests/leavesRequest.html', context)


def request_list(request):
    user = request.user
    employer = Employee.objects.get(user_id=user.id)
    requests_list = []
    options = LeaveRequest.objects.all()
    try:
        for r in options:
            if r.employee_id == employer.id:
                requests_list.append(r)
            else:
                print('err')
    except:
        requests_list = []

    context = {
        'requests_list': requests_list,
        'employer': employer
    }
    print()
    return render(request, 'requests/requestsList.html', context)


def cancel_request(request, id):
    try:
        leave_request = LeaveRequest.objects.get(pk=id)
        leave_request.status = "canceled"
        leave_request.save()
        messages.success(request, 'You have canceled the leave request to your manager successfully !!')
        return redirect('/leave/requestList')

    except:
        msg = "can you try again"
        print(msg)

    return redirect('/leave/requestList')


def update_request(request, id):
    leave_request = LeaveRequest.objects.get(pk=id)
    status =leave_request.status
    employer = leave_request.employee
    manager = leave_request.manager
    form = LeaveRequestForm(request.POST or None, instance=leave_request)
    if form.is_valid():
        leaveRequest = form.save(commit=False)
        leaveRequest.status = status
        leaveRequest.employee = employer
        leaveRequest.manager = manager
        leaveRequest.save()
        messages.success(request, 'You have canceled the leave request to your manager successfully !!')
        return redirect('/leave/requestList')
    context = {
        'form': form
    }
    return render(request, 'requests/editRequest.html', context)
