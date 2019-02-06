from django.shortcuts import render,get_object_or_404,redirect
from leaveManagementApp.models import Employee,LeaveRequest
from akTeams.form.empForms import empForm
from akTeams.form.Userforms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from akTeams.decorators import role_requiredadmin,role_manager
from django.contrib.auth.decorators import login_required
@login_required
@role_requiredadmin()
def index(request):
    list_emp = Employee.objects.all()
    context = {
        'list_emp': list_emp,
    }
    return render(request, 'employees/index.html', context)
#
@login_required
@role_requiredadmin()
def create(request):
    form = empForm(request.POST or None)
    formUser = UserRegisterForm(request.POST or None)
    if formUser.is_valid() and  form.is_valid():

        user = formUser.save(commit=False)
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.email = form.cleaned_data['email']
        empl = form.save(commit=False)
        user.save()
        empl.user = user
        empl.save()
        messages.info(request, 'Employee created')
        return redirect('emp.index')




    context = {
        'form': form,
        'formUser': formUser,
        'modeCreate': True
    }

    return render(request, 'employees/ajoutEmp.html', context)

@login_required
@role_requiredadmin()
def update(request, id):

    item = get_object_or_404(Employee, pk=id)
    form = empForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('emp.index')


    context = {
        'form': form,
        'modeCreate': False
    }
    return render(request, 'employees/ajoutEmp.html', context)

@login_required
@role_requiredadmin()
def delete(request, id):
        item = get_object_or_404(Employee, pk=id)
        item.delete()
        return redirect('emp.index')

@login_required
@role_requiredadmin()
def createUser(request):
    form = UserRegisterForm(request.POST or None)

    if form.is_valid():

        form.save()
        messages.success(request, 'User created')
        return redirect('login')


    context = {
        'form': form,

    }

    return render(request, 'employees/registre.html', context)

@login_required
def dashboard(request):
    empls = Employee.objects.all()
    leaveRequest = LeaveRequest.objects.filter(status='Accepted')
    context = {
        'list_emp': empls,
        'leaveRequest':leaveRequest,
    }
    return render(request, 'dashboard/dashboard.html', context)