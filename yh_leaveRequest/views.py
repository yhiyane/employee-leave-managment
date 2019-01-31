import random
import string

# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from leaveManagementApp.models import LeaveRequest, Employee
from yh_employee.utils import paginate
from yh_leaveRequest.forms import LeaveRequestForm


# Create your views here.


@login_required  # a shortcut to check if user is login
# @user_passes_test(lambda u: u.is_superuser)  # check if the current user is a superuser
# index function to list level study
def index(request):
    # check if get request has keyword param
    employee = Employee.objects.get(user_id=request.user.id)

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']  # store the keyword param into a variable

        if employee.is_manager:
            leave_request_items = LeaveRequest.objects.all()
        else:
            leave_request_items = LeaveRequest.objects.filter(leave_request_code__icontains=keyword,
                                                              employee_id=employee.id)

    else:
        if employee.is_manager:
            leave_request_items = LeaveRequest.objects.filter(manager_id=employee.id)
        else:
            leave_request_items = LeaveRequest.objects.filter(employee_id=employee.id)

        keyword = ""  # set default value for keyword

    paginator = Paginator(leave_request_items, 5)  # Show 5 level studys per page
    pagination = paginate(request, paginator)  # function to get paginated items and items range

    # create a dictionary hold the variables which we send to the template
    context = {
        'items': pagination['page_items'],
        'keyword': keyword,
        'page_range': pagination['page_range'],
    }

    # render the level/index.html template with the context
    return render(request, 'leaveRequest/index.html', context)


@login_required  # a shortcut to check if user is login
# @user_passes_test(lambda u: u.is_superuser)  # check if the current user is a superuser
# show the requested level by id
def show(request, id):
    # get the level study object by id if not found raise a http 404 exception
    item = get_object_or_404(LeaveRequest, pk=id)
    # add the level study object to the context
    if 'validateButton' in request.POST:
        item.status = "ACCEPTED"
        item.save()
        return redirect('leaveRequest.index')
    if 'rejectButton' in request.POST:
        item.status = "REJECTED"
        item.save()
        return redirect('leaveRequest.index')

    context = {
        'item': item
    }
    # render the 'level/show.html' with the context variable
    return render(request, 'leaveRequest/form-manager.html', context)


@login_required  # a shortcut to check if user is login
# @user_passes_test(lambda u: u.is_superuser)  # check if the current user is a superuser
# this function for showing level study form and also for the submission
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


@login_required
def create(request):
    current_user = request.user
    form = LeaveRequestForm(request.POST or None, show_half_day=True)

    # check if the form is valid
    if form.is_valid():
        leave_request = form.save(commit=False)
        # form.leave_request_code = id_generator()
        if Employee.objects.get(user_id=request.user.id) is not None:
            leave_request.employee = Employee.objects.get(user_id=request.user.id)

        leave_request.status = "WAITING"

        leave_request.save()

        messages.info(request, 'leave request created')

        return redirect('leaveRequest.index')

    if Employee.objects.get(user_id=current_user.id) is not None:
        emp_user = Employee.objects.get(user_id=current_user.id)

    context = {
        'form': form,
        'employee': emp_user
    }

    return render(request, 'leaveRequest/form.html', context)


@login_required  # a shortcut to check if user is login
# @user_passes_test(lambda u: u.is_superuser)  # check if the current user is a superuser
# this function for showing level study update form and also for the submission
def update(request, id):
    # get the level study object by id if not found raise a http 404 exception
    item = get_object_or_404(LeaveRequest, pk=id)
    # create LevelForm object fill with inputs if the request method is post or None else
    form = LeaveRequestForm(request.POST or None, instance=item)
    # check if the level study form is valid
    if form.is_valid():
        leave_request = form.save(commit=False)  # save the form into database
        leave_request.employee = Employee.objects.get(user_id=request.user.id)
        leave_request.status = "WAITING"
        item.manager = item.employee.manager
        leave_request.save()
        messages.info(request, 'leave request updated')  # display a message to the user
        return redirect('leaveRequest.index')  # redirect to the level study index

    # add the level study form to the context
    context = {
        'form': form
    }
    # render the 'level/form.html' template with the context
    return render(request, 'leaveRequest/form.html', context)


@login_required  # a shortcut to check if user is login
# @user_passes_test(lambda u: u.is_superuser)  # check if the current user is a superuser
# remove the requested level by id
def delete(request, id):
    # get the level study object by id if not found raise a http 404 exception
    item = get_object_or_404(LeaveRequest, pk=id)

    # check if the request method is POST
    if request.method == 'POST':
        item.delete()  # remove the selected level study
        messages.info(request, 'leave request deleted')  # display success message to the user
        return redirect('leaveRequest.index')  # redirect to the level study index

    messages.info(request, 'something wrong')  # display fail message to the user
    return redirect('leaveRequest.index')  # redirect to the level study index
