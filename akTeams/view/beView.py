from django.shortcuts import render,get_object_or_404,redirect
from leaveManagementApp.models import BusinessEntity
from akTeams.form.beForms import BeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from akTeams.decorators import role_requiredadmin,role_manager
@login_required
@role_requiredadmin()
def index(request):
    list_be = BusinessEntity.objects.all()
    context = {
        'list_be': list_be,
    }
    return render(request, 'businessEntity/index.html', context)
#
@login_required
@role_requiredadmin()
def create(request):
    form = BeForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'businessEntity created')
        return redirect('be.index')

    context = {
        'form': form,
        'modeCreate': True
    }

    return render(request, 'businessEntity/formBe.html', context)
#
@login_required
@role_requiredadmin()
def update(request, id):

    item = get_object_or_404(BusinessEntity, pk=id)
    form = BeForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('be.index')


    context = {
        'form': form,
        'modeCreate': False
    }
    return render(request, 'businessEntity/formBe.html', context)
#
@login_required
@role_requiredadmin()
def delete(request, id):
        item = get_object_or_404(BusinessEntity, pk=id)
        item.delete()
        return redirect('be.index')