from django.shortcuts import render,get_object_or_404,redirect
from leaveManagementApp.models import Position
from akTeams.form.PositionForms import PositionForm
from akTeams.decorators import role_requiredadmin,role_manager
from django.contrib.auth.decorators import login_required
@login_required
@role_requiredadmin()
def index(request):

    list_position = Position.objects.all()
    context = {
        'list_position': list_position,
    }
    return render(request, 'postion/index.html', context)

@login_required
@role_requiredadmin()
def create(request):
    form = PositionForm(request.POST or None)
    if form.is_valid():
        form.save()
        # messages.info(request, 'Team created')
        return redirect('position.index')

    context = {
        'form': form,
        'modeCreate': True
    }

    return render(request, 'postion/formPosition.html', context)

@login_required
@role_requiredadmin()
def update(request, id):

    item = get_object_or_404(Position, pk=id)
    form = PositionForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('position.index')


    context = {
        'form': form,
        'modeCreate': False
    }
    return render(request, 'postion/formPosition.html', context)

@login_required
@role_requiredadmin()
def delete(request, id):
        item = get_object_or_404(Position, pk=id)
        item.delete()
        return redirect('position.index')