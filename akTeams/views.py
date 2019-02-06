from django.shortcuts import render,get_object_or_404,redirect
from leaveManagementApp.models import Team
from .form.forms import TeamForm
from akTeams.form.membreTeamForms import MemberTeamForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from akTeams.decorators import role_requiredadmin
# Create your views here.

@login_required
@role_requiredadmin()
def index(request):
    # form = TeamForm(request.POST or None)
    list_teams = Team.objects.all()
    context = {
        'list_teams': list_teams,
    }
    return render(request, 'team/index.html', context)


@login_required
@role_requiredadmin()
def create(request):
    form = TeamForm(request.POST or None)
    if form.is_valid():
        form.save()
        # messages.info(request, 'Team created')
        return redirect('team.index')

    context = {
        'form': form,
        'modeCreate': True
    }

    return render(request, 'team/ajoutTeam.html', context)
@login_required
@role_requiredadmin()
def update(request, id):

    item = get_object_or_404(Team, pk=id)
    form = TeamForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('team.index')


    context = {
        'form': form,
        'modeCreate': False
    }
    return render(request, 'team/ajoutTeam.html', context)
@login_required
@role_requiredadmin()
def delete(request, id):

        item = get_object_or_404(Team, pk=id)
        item.delete()
        return redirect('team.index')

@login_required
@role_requiredadmin()
def affectation(request, id):

    item = get_object_or_404(Team, pk=id)

    form = MemberTeamForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('team.index')


    context = {
        'form': form,
        'teamSelected':item

    }
    return render(request, 'membreTeam/affectation.html', context)
