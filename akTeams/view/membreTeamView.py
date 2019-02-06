from django.shortcuts import render,get_object_or_404,redirect
from leaveManagementApp.models import Employee,Team
from akTeams.form.membreTeamForms import MemberTeamForm,MTeamForm
from akTeams.decorators import role_requiredadmin,role_manager
from django.contrib.auth.decorators import login_required
@login_required
@role_requiredadmin()
def create(request):
    form = MTeamForm(request.POST or None)

    print(request.GET.get('teams'))
    if form.is_valid():
        teams = form.cleaned_data['teams']
        members = form.cleaned_data['members']

        print('test')
        # print(Team.objects.get(id = answer['teams'].))
        teams.members.clear()
        teams.members.add(*members)

        print(members)
        print(teams.members.all())
        # form.save()
        # messages.info(request, 'Team created')
        return redirect('membreTeam.create')

    context = {
        'form': form,
    }

    return render(request, 'membreTeam/affectation.html', context)


@login_required
@role_requiredadmin()
def load_membres(request):

    test = []
    team_id = request.GET.get('teamSelected')
    print(team_id)

    team = Team.objects.get(id = team_id)

    membres = team.members.all()
    all = Employee.objects.exclude(id__in = membres)
    context = {
        'membres': membres,
        'all': all,
    }


    return render(request, 'membreTeam/membresLoad.html' ,  context)


