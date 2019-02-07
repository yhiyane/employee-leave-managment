import self as self
from django.shortcuts import render, redirect
from .forms import LeaveRequestForm
from .models import Employee, LeaveRequest, Notifications
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def send_notification(created_by, created_to, title, id_leaveRequest):
    leave_request = LeaveRequest.objects.get(pk=id_leaveRequest)
    # add new notification
    notification = Notifications.objects.create(
        title=title,
        created_by=created_by,
        created_to=created_to,
        leave_request=leave_request
    )
    notification.save()
    return notification


@login_required
def index_leave(request):
    if request.method == 'POST':
        user = request.user
        employer = Employee.objects.get(user_id=user.id)
        form = LeaveRequestForm(request.POST or None)
        manager = Employee.objects.get(id=employer.manager_id)
        if form.is_valid():
            leave_request = form.save(commit=False)
            leave_request.employee = employer
            leave_request.manager = manager
            leave_request.status = "waiting"
            leave_request.save()
            # add new notification
            title = employer.first_name + ' ' + manager.last_name + ' sent you an new leave request'
            send_notification(employer, manager, title, leave_request.id)
            messages.success(request, 'You have sent the leave request to your manager successfully !!')
            return redirect('/leave/requestList')
        else:
            print('test:', form.errors)

    else:
        form = LeaveRequestForm()

    context = {
        'form': form
    }
    return render(request, 'requests/leavesRequest.html', context)


@login_required
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


@login_required
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


@login_required
def update_request(request, id):
    leave_request = LeaveRequest.objects.get(pk=id)
    status = leave_request.status
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


def get_user_notifications(request):
    user = request.user
    new_notifications = []
    try:
        employer_user = Employee.objects.get(user_id=user.id)
        for n in Notifications.objects.all():
            if n.created_to_id == employer_user.id and n.tag_vu is False:
                new_notifications.append(n)
        count = len(new_notifications)
        if count == 0:
            context = {
                'notifications': new_notifications
            }
        else:
            context = {
                'notifications': new_notifications,
                'count': count
            }
        return context
    except:
        context = {
            'notifications': []
        }
        print('test')
        return context


def accept_refuse(id, choice):
    leave_request = LeaveRequest.objects.get(pk=id)
    leave_request.status = choice
    leave_request.save()
    return leave_request.status


@login_required
def show_notification_manager(request, id):
    user = request.user
    employee = Employee.objects.get(user_id=user.id)
    id_user = str(employee.id)
    try:
        # notification
        notification = Notifications.objects.get(pk=id)
        notification.tag_vu = True
        notification.save()
        # employer
        employer = Employee.objects.get(pk=notification.created_by_id)
        # leave request
        leave_request = LeaveRequest.objects.get(pk=notification.leave_request_id)
        form = LeaveRequestForm(request.POST or None)
        if request.method == 'POST' and 'refuse' in request.POST:
            accept_refuse(leave_request.id, 'rejected')
            title = 'Your manager ' + employee.first_name + ' ' + employer.last_name + ' refuse your leave request'
            send_notification(employee, employer, title, leave_request.id)
            return redirect('/leave/employers_requests/' + id_user)
        if request.method == 'POST' and 'accept' in request.POST:
            accept_refuse(leave_request.id, 'accepted')
            title = 'Your manager ' + employee.first_name + ' ' + employer.last_name + ' accept your leave request'
            send_notification(employee, employer, title, leave_request.id)
            return redirect('/leave/employers_requests/' + id_user)
        context = {
            'employer': employer,
            'leave_request': LeaveRequest.objects.get(pk=notification.leave_request_id),
            'profile_employer': User.objects.get(pk=employer.user_id)
        }
        return render(request, 'requests/employer_request.html', context)
    except:
        print('err')
        return render(request, 'requests/employer_request.html')


@login_required
def update_employer_request(request, id):
    user = request.user
    employee = Employee.objects.get(user_id=user.id)
    leave_request = LeaveRequest.objects.get(pk=id)
    form = LeaveRequestForm(request.POST or None)
    id_user = str(employee.id)
    # employer
    employer = Employee.objects.get(pk=leave_request.employee_id)
    if request.method == 'POST' and 'refuse' in request.POST:
        accept_refuse(leave_request.id, 'rejected')
        return redirect('/leave/employers_requests/' + id_user)
    if request.method == 'POST' and 'accept' in request.POST:
        accept_refuse(leave_request.id, 'accepted')
        return redirect('/leave/employers_requests/' + id_user)
    context = {
        'employer': employer,
        'leave_request': leave_request,
        'profile_employer': User.objects.get(pk=employer.user_id)
    }
    return render(request, 'requests/employer_request.html', context)


@login_required
def delete_employer_request(request, id):
    user = request.user
    employee = Employee.objects.get(user_id=user.id)
    if employee.tag_manager is True:
        leave_request = LeaveRequest.objects.get(pk=id)
        leave_request.delete()
        id_user = str(employee.id)
        return redirect('/leave/employers_requests/' + id_user)
    else:
        return render(request, 'users/forbideen.html')


@login_required
def employers_requests(request, id):
    user = request.user
    employee = Employee.objects.get(user_id=user.id)
    if employee.tag_manager is True:
        requests_list = LeaveRequest.objects.filter(manager_id=id)
        context = {
            'requests_list': requests_list
        }
        return render(request, 'requests/employers_requests.html', context)
    else:
        return render(request, 'users/forbideen.html')
