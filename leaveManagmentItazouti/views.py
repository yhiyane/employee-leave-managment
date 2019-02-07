from django.shortcuts import render,redirect
from .models import *
from leaveManagmentItazouti import forms
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.

#Employee
@login_required
def home(request):
    employee = Employee.objects.all()
    context = {
        'employee': employee
    }
    return render(request, 'crud_app/employee_list.html', context)


def connect(request):

    employee = Employee.objects.all()
    context = {
        'employee': employee
    }
    return render(request, 'crud_app/employee_list.html', context)


def disconnect(request):
    logout(request)
    return render(request, 'crud_app/registration/login.html')


def delete_employee(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    messages.error(request, 'Employé supprimé.')
    return redirect('/leave/')


def add_emp(request):
    form_data = forms.employeeForm(request.POST or None)
    context = {
        'form_data': form_data
    }
    if form_data.is_valid():
        emp = form_data.save(commit=False)
        emp.save()
        id_emp = str(emp.id)
        print('test',id_emp)
        messages.success(request, 'Employé ajouté.')
        return redirect('/register/'+ id_emp)
    return render(request, 'crud_app/add_employee.html', context)


def update_emp(request, id):
    instance = Employee.objects.get(pk=id)
    form_data = forms.employeeForm(request.POST or None, instance=instance)
    context = {
        'form_data': form_data
    }
    if form_data.is_valid():
        form_data.save()
        messages.success(request, 'Employé modifié.')
        return redirect('/leave/')

    return render(request, 'crud_app/add_employee.html', context)

#Team
def team_index(request):
    teams = Team.objects.all()
    context = {
        'teams': teams
    }
    return render(request, 'crud_app/teams_list.html', context)


def add_team(request):
    form_data = forms.teamForm(request.POST or None)
    if form_data.is_valid():
        form_data.save()
        messages.success(request, 'Equipe ajoutée.')
        return redirect('/leave/team_index/')
    context = {
        'form_data': form_data
    }
    return render(request, 'crud_app/add_team.html', context)


def delete_team(request, id):
    team = Team.objects.get(pk=id)
    team.delete()
    messages.error(request, 'Equipe supprimée.')
    return redirect('/leave/team_index/')


def update_team(request, id):
    instance = Team.objects.get(pk=id)
    form_data = forms.teamForm(request.POST or None, instance=instance)
    context = {
        'form_data': form_data
    }
    if form_data.is_valid():
        form_data.save()
        messages.success(request, 'Equipe modifiée.')
        return redirect('/leave/team_index/')

    return render(request, 'crud_app/add_team.html', context)

#position

def position_index(request):
    positions = Position.objects.all()
    context = {
        'positions': positions
    }
    return render(request, 'crud_app/positions_list.html', context)


def add_position(request):
    form_data = forms.positionForm(request.POST or None)
    if form_data.is_valid():
        form_data.save()
        messages.success(request, 'Position ajoutée.')
        return redirect('/leave/position_index/')
    context = {
        'form_data': form_data
    }
    return render(request, 'crud_app/add_position.html', context)


def delete_position(request, id):
    position = Position.objects.get(pk=id)
    position.delete()
    messages.error(request, 'Position supprimée.')
    return redirect('/leave/position_index/')


def update_position(request, id):
    instance = Position.objects.get(pk=id)
    form_data = forms.positionForm(request.POST or None, instance=instance)
    context = {
        'form_data': form_data
    }
    if form_data.is_valid():
        form_data.save()
        messages.success(request, 'Position modifiée.')
        return redirect('/leave/position_index/')

    return render(request, 'crud_app/add_position.html', context)

#Be

def be_index(request):
    businessEntities = BusinessEntity.objects.all()
    context = {
        'businessEntities': businessEntities
    }
    return render(request, 'crud_app/be_list.html', context)


def add_be(request):
    form_data = forms.beForm(request.POST or None)
    if form_data.is_valid():
        form_data.save()
        messages.success(request, 'Entreprise ajoutée.')
        return redirect('/leave/be_index/')
    context = {
        'form_data': form_data
    }
    return render(request, 'crud_app/add_be.html', context)


def delete_be(request, id):
    be = BusinessEntity.objects.get(pk=id)
    be.delete()
    messages.error(request, 'Entreprise supprimée.')
    return redirect('/leave/be_index/')


def update_be(request, id):
    instance = BusinessEntity.objects.get(pk=id)
    form_data = forms.beForm(request.POST or None, instance=instance)
    context = {
        'form_data': form_data
    }
    if form_data.is_valid():
        form_data.save()
        messages.success(request, 'Entreprise modifiée.')
        return redirect('/leave/be_index/')

    return render(request, 'crud_app/add_be.html', context)


def leave_index(request):
    user = request.user
    leaves = Leave.objects.all()
    leaveRequest = LeaveRequest.objects.all()
    if user.is_superuser:
        context = {
            'leaves': leaves,
            'leaveRequest': leaveRequest
        }
        return render(request, 'crud_app/leave_list.html', context)
    else:
        try:
            employer = get_object_or_404(Employee, user_id=user.id)
            my_leave_request = []
            my_leave = []
            for lr in leaveRequest:
                if lr.employee.id == employer.id:
                    my_leave_request.append(lr)
            for leave in leaves:
                if leave is not None and leave.leave_request is not None:
                    if leave.leave_request.employee.id == employer.id:
                        my_leave.append(leave)
            context = {
                'leaves': my_leave,
                'leaveRequest': my_leave_request
            }
            return render(request, 'crud_app/leave_list.html', context)
        except:
            return render(request, 'crud_app/employee_list.html', context)


def leave_request(request):
    form_data = forms.leaveRequestForm(request.POST or None)

    if form_data.is_valid():
        form_data.save()
        messages.success(request, 'Demande ajoutée.')
        return redirect('/leave/leave_index/')
    context = {
        'form_data': form_data
    }
    return render(request, 'crud_app/leave_request.html', context)


def update_leave_request(request, id):
    instance = LeaveRequest.objects.get(pk=id)
    form_data = forms.leaveRequestForm(request.POST or None, instance=instance)
    context = {
        'form_data': form_data
    }
    if form_data.is_valid():
        form_data.save()
        messages.success(request, 'Demande modifiée.')
        return redirect('/leave/leave_index/')

    return render(request, 'crud_app/leave_request.html', context)


def delete_leave_request(request, id):
    leave_request = LeaveRequest.objects.get(pk=id)
    leave_request.delete()
    messages.error(request, 'Demande supprimée.')
    return redirect('/leave/leave_index/')



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('home')
    else:
        form = UserCreationForm()
    context={
        'form' : form
    }

    return render(request,'registration/register.html', context)