from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Team, BusinessUnit, Position
from .forms import EmployerRegister, EditForm, TeamForm, BUForm, PositionForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


def getUser(request):
    user = request.user
    employer = Employee.objects.get(user_id=user.id)
    context ={
        'employer':employer
    }
    return context


@login_required
def index(request):
    user = request.user
    employer = Employee.objects.get(user_id=user.id)
    if employer.tag_manager is True:
        context = {
            'employers': Employee.objects.all(),
            'employer': employer,

        }

        return render(request, 'employers/employerList.html', context)
    else:
        return redirect('/setting/profile')


# delete function
@login_required
def delete(request, id):
    user = request.user
    employer = Employee.objects.get(user_id=user.id)
    if employer.tag_manager is True:
        employer = Employee.objects.get(pk=id)
        employer.delete()
        return redirect('/setting')
    else:
        return render(request, 'users/forbideen.html')


@login_required
def create(request):
    user = request.user
    employer = Employee.objects.get(user_id=user.id)
    if employer.tag_manager is True:
        if request.method == "POST":
            my_form = EmployerRegister(request.POST)
            if my_form.is_valid():
                # now the data is good
                # bu selected
                be = BusinessUnit.objects.get(pk=my_form.cleaned_data['be'])
                position = Position.objects.get(pk=my_form.cleaned_data['position'])
                employer = Employee.objects.create(
                    first_name=my_form.cleaned_data['first_name'],
                    last_name=my_form.cleaned_data['last_name'],
                    cin_code=my_form.cleaned_data['cin_code'],
                    birth_date=my_form.cleaned_data['birth_date'],
                    hire_date=my_form.cleaned_data['hire_date'],
                    email=my_form.cleaned_data['email'],
                    cnss_code=my_form.cleaned_data['cnss_code'],
                    experience_years_number=my_form.cleaned_data['experience_years_number'],
                    be=be,
                    positon=position,
                    tag_manager=my_form.cleaned_data['tag_manager'],
                )

                try:
                    manager = Employee.objects.get(pk=my_form.cleaned_data['managers'])
                    employer.manager = manager
                    employer.save()
                    print('test', my_form.cleaned_data['managers'])
                except:
                    pass
                for id_team in my_form.cleaned_data['team']:
                    team = Team.objects.get(pk=id_team)
                    employer.team.add(team)
            else:
                print(my_form.errors)
        messages.info(request, 'You have added  new employer successfully.')
        context = {
            'id_employer': employer.id
        }
        id = str(employer.id)
        return redirect('/setting/register/' + id)
    else:
        return render(request, 'users/forbideen.html')


@login_required
def add_newEmployer(request):
    user = request.user
    employer = Employee.objects.get(user_id=user.id)
    if employer.tag_manager is True:
        my_form = EmployerRegister()
        context = {
            'form': my_form
        }
        return render(request, 'employers/add_newEmployer.html', context)
    else:
        return render(request, 'users/forbideen.html')


@login_required
def register(request, id):
    user = request.user
    employer = Employee.objects.get(user_id=user.id)
    if employer.tag_manager is True:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST or None)
            print(form)
            if form.is_valid():
                user = form.save(commit=False)
                user.save()
                employee = get_object_or_404(Employee, pk=id)
                employee.user = user
                employee.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}!')
                return redirect('/setting/')
        else:
            form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})
    else:
        return render(request, 'users/forbideen.html')


@login_required
def edit(request, id):
    user = request.user
    employer = Employee.objects.get(user_id=user.id)
    if employer.tag_manager is True:
        employee = get_object_or_404(Employee, pk=id)
        form = EditForm(request.POST or None, instance=employee)
        if form.is_valid():
            form.save()
            messages.info(request, 'You have updated  this element successfully.')
        context = {
            'form': form,
            'employee': employee
        }
        return render(request, 'employers/edit.html', context)
    else:
        return render(request, 'users/forbideen.html')


@login_required
def teams(request):
    user = request.user
    if user.is_superuser is True:
        allTeams = Team.objects.all()
        form_team = TeamForm()
        context = {
            'teams': allTeams,
            'form_team': form_team
        }
        return render(request, 'teams/teamsList.html', context)
    else:
        return render(request, 'users/forbideen.html')


@login_required
def delete_team(request, id):
    user = request.user
    if user.is_superuser is True:
        team = Team.objects.get(pk=id)
        team.delete()
        messages.info(request, 'You have deleted this element successfully.')
        return redirect('/setting/teams')
    else:
        return render(request, 'users/forbideen.html')


@login_required
def add_teams(request):
    user = request.user
    if user.is_superuser is True:
        if request.method == "POST":
            form = TeamForm(request.POST)
            if form.is_valid():
                form.save()
        messages.info(request, 'You have added new element successfully.')
        return redirect('/setting/teams')
    else:
        return render(request, 'users/forbideen.html')


@login_required
def find_team(request, id):
    user = request.user
    if user.is_superuser is True:
        team = Team.objects.get(pk=id)
        context = {
            'teamf': team
        }
        return render(request, 'teams/delete_team.html', context)
    else:
        return render(request, 'users/forbideen.html')


@login_required
def edit_team(request, id):
    user = request.user
    if user.is_superuser is True:
        team = get_object_or_404(Team, pk=id)
        form = TeamForm(request.POST or None, instance=team)
        if form.is_valid():
            form.save()

        context = {
            'form_edit': form,
            'team': team
        }
        messages.info(request, 'You have updated this element successfully.')
        return render(request, 'teams/edit_team.html', context)
    else:
        return render(request, 'users/forbideen.html')


@login_required
def bu(request):
    user = request.user
    if user.is_superuser is True:
        all_bu = BusinessUnit.objects.all()
        form_add = BUForm()
        context = {
            'buList': all_bu,
            'form': form_add
        }
        return render(request, 'bu/buList.html', context)
    else:
        return render(request, 'users/forbideen.html')


@login_required
def add_bu(request):
    user = request.user
    if user.is_superuser is True:
        if request.method == "POST":
            form = BUForm(request.POST)
            if form.is_valid():
                form.save()
        messages.info(request, 'You have added new element successfully.')
        return redirect('/setting/bu')
    else:
        return render(request, 'users/forbideen.html')


@login_required
def edit_bu(request, id):
    user = request.user
    if user.is_superuser is True:
        bu = get_object_or_404(BusinessUnit, pk=id)
        form = BUForm(request.POST or None, instance=bu)
        if form.is_valid():
            form.save()

        context = {
            'form_edit': form,
            'bu': bu
        }
        messages.info(request, 'You have updated this element successfully.')
        return render(request, 'bu/edit_bu.html', context)
    else:
        return render(request, 'users/forbideen.html')


@login_required
def find_bu(request, id):
    user = request.user
    if user.is_superuser is True:
        bu = BusinessUnit.objects.get(pk=id)
        context = {
            'bu': bu
        }
        return render(request, 'bu/delete.html', context)
    else:
        return render(request, 'users/forbideen.html')


@login_required
def delete_bu(request, id):
    user = request.user
    if user.is_superuser is True:
        bu = BusinessUnit.objects.get(pk=id)
        bu.delete()
        messages.info(request, 'You have deleted this element successfully.')
        return redirect('/setting/bu')
    else:
        return render(request, 'users/forbideen.html')


@login_required
def position(request):
    user = request.user
    if user.is_superuser is True:
        all_position = Position.objects.all()
        form_add = PositionForm()
        context = {
            'positions': all_position,
            'form': form_add
        }
        return render(request, 'position/positionsList.html', context)
    else:
        return render(request, 'users/forbideen.html')


@login_required
def add_position(request):
    user = request.user
    if user.is_superuser is True:
        user = request.user
        if user.is_superuser is True:
            if request.method == "POST":
                form = PositionForm(request.POST)
                if form.is_valid():
                    form.save()
            messages.info(request, 'You have added new element successfully.')
            return redirect('/setting/position')

    else:
        return render(request, 'users/forbideen.html')


@login_required
def edit_position(request, id):
    user = request.user
    if user.is_superuser is True:
        p = get_object_or_404(Position, pk=id)
        form = PositionForm(request.POST or None, instance=p)
        if form.is_valid():
            form.save()
            messages.info(request, 'You have updated this element successfully.')
            return redirect('/setting/position')
        context = {
            'form_edit': form,
            'position': position
        }

        return render(request, 'position/edit_position.html', context)
    else:
        return render(request, 'users/forbideen.html')


@login_required
def find_position(request, id):
    user = request.user
    if user.is_superuser is True:
        p = Position.objects.get(pk=id)
        context = {
            'position': p
        }
        return render(request, 'position/delete.html', context)
    else:
        return render(request, 'users/forbideen.html')


@login_required
def delete_position(request, id):
    user = request.user
    if user.is_superuser is True:
        p = Position.objects.get(pk=id)
        p.delete()
        messages.info(request, 'You have deleted this element successfully.')
        return redirect('/setting/position')
    else:
        return render(request, 'users/forbideen.html')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('/setting/profile/')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
