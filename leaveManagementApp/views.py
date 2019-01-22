# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from yh_be.forms import BEForm
from leaveManagementApp.models import BusinessEntity
from yh_employee.utils import paginate


# Create your views here.


@login_required  # a shortcut to check if user is login
@user_passes_test(lambda u: u.is_superuser)  # check if the current user is a superuser
# index function to list business unit
def index(request):
    # check if get request has keyword param
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']  # store the keyword param into a variable
        bu_items = BusinessEntity.objects.filter(libelle_icontains=keyword)  # like %keyword%
    else:
        bu_items = BusinessEntity.objects.all()  # get all business units items
        keyword = ""  # set default value for keyword

    paginator = Paginator(bu_items, 5)  # Show 5 business units per page
    pagination = paginate(request, paginator)  # function to get paginated items and items range

    # create a dictionary hold the variables which we send to the template
    context = {
        'items': pagination['page_items'],
        'keyword': keyword,
        'page_range': pagination['page_range'],
    }

    # render the bu/index.html template with the context
    return render(request, 'be/index.html', context)


@login_required  # a shortcut to check if user is login
@user_passes_test(lambda u: u.is_superuser)  # check if the current user is a superuser
# show the requested business unit by id
def show(request, id):
    # get the business unit object by id if not found raise a http 404 exception
    item = get_object_or_404(BusinessEntity, pk=id)
    # add the business unit object to the context
    context = {
        'item': item
    }
    # render the 'bu/show.html' with the context variable
    return render(request, 'be/show.html', context)


@login_required  # a shortcut to check if user is login
@user_passes_test(lambda u: u.is_superuser)  # check if the current user is a superuser
# this function for showing business unit form and also for the submission
def create(request):
    # create BUForm object fill with inputs if the request method is post or None else
    form = BEForm(request.POST or None)
    # check if the form is valid
    if form.is_valid():
        form.save()  # save the input values into database
        #  display notification message to user
        messages.info(request, 'business entity created')
        # redirect to the business unit index
        return redirect('be.index')

    # add the business unit form to the context
    context = {
        'form': form
    }

    # render the 'bu/form.html'  template with the context
    return render(request, 'be/form.html', context)


@login_required  # a shortcut to check if user is login
@user_passes_test(lambda u: u.is_superuser)  # check if the current user is a superuser

# this function for showing business unit update form and also for the submission
def update(request, id):
    # get the business unit object by id if not found raise a http 404 exception
    item = get_object_or_404(BusinessEntity, pk=id)

    # create BUForm object fill with inputs if the request method is post or None else
    # pass the business unit object to the form
    form = BEForm(request.POST or None, instance=item)
    # check if the business unit form is valid
    if form.is_valid():
        form.save()  # save the form into database
        messages.info(request, 'business entity updated')  # display a message to the user
        return redirect('be.index')  # redirect to the business unit index

    # add the business unit form to the context
    context = {
        'form': form
    }
    # render the 'bu/form.html' template with the context
    return render(request, 'be/form.html', context)


@login_required  # a shortcut to check if user is login
@user_passes_test(lambda u: u.is_superuser)  # check if the current user is a superuser
# remove the requested business unit by id
def delete(request, id):
    # get the business unit object by id if not found raise a http 404 exception
    item = get_object_or_404(BusinessEntity, pk=id)

    # check if the request method is POST
    if request.method == 'POST':
        item.delete()  # remove the selected business unit
        messages.info(request, 'business entity deleted')  # display success message to the user
        return redirect('be.index')  # redirect to the business unit index

    messages.info(request, 'something wrong')  # display fail message to the user
    return redirect('be.index')  # redirect to the business unit index
