import csv

import xlrd as xlrd
import xlwt as xlwt
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

from leaveManagementApp.models import BusinessEntity
from leaveManagementApp.models import Employee
from yh_employee.forms import EmployeeForm, ExportForm
from yh_employee.models import Document
from yh_employee.utils import paginate
# employee list
from yh_user.forms import UserForm


# from employee.forms import employeeForm, DocumentForm, ExportForm
# Create your views here.


@login_required  # a shortcut to check if user is login
def index(request):  # index function to list employees
    # check if get request has keyword param
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']  # store the keyword param into a variable
        # search by first name or last name
        employees_items = Employee.user.objects.filter(
            Q(first_name__icontains=keyword) | Q(last_name__icontains=keyword))
    else:
        employees_items = Employee.objects.all()  # get all employee
        keyword = ""

    paginator = Paginator(employees_items, 10)  # Show 10 employees per page
    pagination = paginate(request, paginator)  # function to get paginated items and items range

    # create a dictionary hold the variables which we send to the template
    context = {
        'items': pagination['page_items'],
        'keyword': keyword,
        'page_range': pagination['page_range'],
    }

    # render the employee/index.html template with the context
    return render(request, 'employee/index.html', context)


@login_required
# show the requested employee by id and his documents
def show(request, id):
    # get the employee object by id if not found raise a http 404 exception
    item = get_object_or_404(Employee, pk=id)
    context = {
        'item': item
    }
    return render(request, 'employee/show.html', context)


@login_required
# this function for showing employee form and documents form and also for the form submission of those forms
def create(request):
    form = EmployeeForm()  # create SalariedForm object
    userForm = UserForm()  # create SalariedForm object
    employee = Employee()
    if request.method == 'GET':  # check if get request
        context = {
            'form': form,
            'userForm': userForm
        }
        return render(request, 'employee/form.html', context)

    if request.method == 'POST':  # check if post request
        form = EmployeeForm(request.POST)  # fill the form object with inputs if the request method
        userForm = UserForm(request.POST)  # fill the form object with inputs if the request method
        # check if the Employee form is valid and also the document formset is valid
        if form.is_valid() and userForm.is_valid():
            uf = userForm.save()
            emp = form.save(commit=False)
            print("employee form==> ")
            print(emp)
            emp.user = uf  # employee
            emp.first_name = uf.first_name
            emp.last_name = uf.last_name
            emp.save()
            form.save_m2m()
            messages.info(request, 'new employee created')
            return redirect('employee.index')
        else:
            context = {
                'form': form,
                'userForm': userForm
            }
            return render(request, 'employee/form.html', context)


@login_required
# this function for showing employee update form and also for the form submission
def update(request, id):
    item = get_object_or_404(Employee, pk=id)
    # create SalariedForm object
    userForm = UserForm()
    form = EmployeeForm(request.POST or None, instance=item)  # pass the Employee instance to the form
    userForm = UserForm(request.POST or None, instance=item.user)  # pass the Employee instance to the form
    if form.is_valid() and userForm.is_valid():
        uf = userForm.save()
        emp = form.save(commit=False)
        emp.user = uf  # employee
        emp.first_name = uf.first_name
        emp.last_name = uf.last_name
        emp.save()
        form.save_m2m()
        messages.info(request, 'employee updated')
        return redirect('employee.index')

    context = {
        'form': form,
        'userForm': userForm,
        'item': item
    }
    return render(request, 'employee/form-update.html', context)


@login_required
# remove the selected employee by id
def delete(request, id):
    item = get_object_or_404(Employee, pk=id)
    if request.method == 'POST':
        item.delete()
        messages.info(request, 'employee removed')
        return redirect('employee.index')
    return redirect('employee.index')


@login_required
# remove the selected document by employee id and document id
def delete_document(request, employee_id, document_id):
    item = get_object_or_404(Employee, pk=employee_id)
    try:  # check if the employee has the selected document
        document = item.document_set.get(id=document_id)
    except Document.DoesNotExist:  # if the document doesn't exist raise Http404
        raise Http404("Document Does Not Exist")
    if request.method == 'POST':
        document.delete()
        messages.info(request, 'document removed')
        return redirect('employee.documents.index', employee_id)
    return redirect('employee.show', employee_id)


# @login_required
# generate a form to create a new document for a given employee and his submission
# def create_document(request, employee_id):
#     item = get_object_or_404(Employee, pk=employee_id)  # select the employee
#     form = DocumentForm(request.POST or None, request.FILES or None)  # fill the form if the request method is post
#     if form.is_valid():  # check the document form if is valid
#         fd = form.save(commit=False)
#         fd.employee = item
#         fd.save()
#         messages.info(request, 'document created')
#         return redirect('employee.documents.index', item.id)
#     context = {
#         'form': form,
#         'item': item
#     }
#     # render the 'employee/document-form.html' with employee form and employee object
#     return render(request, 'employee/document-form.html', context)

# @login_required
# form for update document of a given employee and his submission
# def update_document(request, employee_id, document_id):
#     item = get_object_or_404(Employee, pk=employee_id)  # find the employee or raise an exception
#
#     try:  # find the document or raise an exception
#         document_item = item.document_set.get(id=document_id)
#     except Document.DoesNotExist:
#         raise Http404("Document Does Not Exist")
#
#     form = DocumentForm(request.POST or None, instance=document_item)  # pass the Document instance to Document form
#     if form.is_valid():
#         fd = form.save(commit=False)
#         fd.employee = item  # add employee to the document
#         fd.save()
#         messages.info(request, 'document updated')
#         return redirect('employee.documents.index', item.id)
#     context = {
#         'form': form,
#         'item': item
#     }
#     return render(request, 'employee/document-form.html', context)

@login_required
# list all documents for a given employee
def index_document(request, employee_id):
    # get the employee object by id if not found raise a http 404 exception
    item = get_object_or_404(Employee, pk=employee_id)
    documents = item.document_set.all()

    context = {
        'documents': documents,
        'item': item,
    }

    # render the template with context variable
    return render(request, 'employee/document-index.html', context)


@login_required
# export all employees as xls format
def export_employee_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="employee.xls"'  # file name

    wb = xlwt.Workbook(encoding='utf-8')  # encodage
    ws = wb.add_sheet('employee')  # add new sheet and name it

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Id', 'First name', 'Last name', 'Cin Code', 'BirthDay', 'HireDay', 'Email', 'Cnss Code',
               'Experience years number',
               'Level Study', 'Degree Study', 'Business Unit']  # header list

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)  # add each header to the first row

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()  # general style
    date_format = xlwt.XFStyle()  # style the date
    date_format.num_format_str = 'yyyy-mm-dd'  # date format

    rows = Employee.objects.all()  # get all employees

    # write each row to the excel
    for row, o in enumerate(rows):
        ws.write(row + 1, 0, o.id, font_style)
        ws.write(row + 1, 1, o.first_name, font_style)
        ws.write(row + 1, 2, o.last_name, font_style)
        ws.write(row + 1, 3, o.cin_code, font_style)
        ws.write(row + 1, 4, o.birth_day, date_format)
        ws.write(row + 1, 5, o.hire_day, date_format)
        ws.write(row + 1, 6, o.email, font_style)
        ws.write(row + 1, 7, o.cnss_code, font_style)
        ws.write(row + 1, 8, o.experience_years_number, font_style)
        ws.write(row + 1, 9, None if o.level_study is None else o.level_study.name, font_style)
        ws.write(row + 1, 10,
                 None if o.degrees_study is None else ';'.join(item.name for item in o.degrees_study.all() if item),
                 font_style)
        ws.write(row + 1, 11, None if o.bu is None else o.bu.name, font_style)

    wb.save(response)  # save the excel to response
    return response


@login_required
# export all employees as csv format
def export_employee_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="employee.csv"'

    writer = csv.writer(response, delimiter=';')
    writer.writerow(
        ['Id', 'First name', 'Last name', 'Cin Code', 'BirthDay', 'HireDay', 'Email', 'Cnss Code',
         'Experience years number',
         'Level Study', 'Degree Study', 'Business Unit']
    )

    users = Employee.objects.all()
    for user in users:
        writer.writerow(
            [
                user.id,
                user.first_name,
                user.last_name,
                user.cin_code,
                user.birth_day,
                user.hire_day,
                user.email,
                user.cnss_code,
                user.experience_years_number,
                None if user.level_study is None else user.level_study.name,
                None if user.degrees_study is None else ','.join(
                    item.name for item in user.degrees_study.all() if item),
                None if user.bu is None else user.bu.name
            ]
        )
    return response


@login_required
# import employees from csv or xls file
def import_employee_index(request):
    form = ExportForm(request.POST or None, request.FILES or None)  # create a employees form
    list = []
    if form.is_valid():  # check if is valid
        # form.save()
        data = form.files.get("attached_piece")  # get the added file
        valid = 0  # to count valid rows
        invalid = 0  # to count invalid rows

        if data.name.endswith('.xls'):  # if the file is xls
            book = xlrd.open_workbook(data.name, file_contents=data.read())
            first_sheet = book.sheet_by_index(0)  # select the first sheet
            if first_sheet.nrows == 1 or first_sheet.nrows == 0:
                messages.info(request, "no rows found")
                return redirect('employee.import_employee_index')

            for r in range(first_sheet.nrows):  # iterate over sheet rows
                if r == 0:  # pass the first row
                    pass
                else:
                    row = first_sheet.row_values(r)  # select the row values
                    errors = []
                    try:
                        degrees_study = row[10].split(";")
                        degrees_study_list = []
                        # for degree in degrees_study:
                        #     degree_study_tmp = Degree.objects.get(name=degree)
                        #     degrees_study_list.append(degree_study_tmp)
                        # level_study = Level.objects.get(name=row[9])
                        # bu = BU.objects.get(name=row[11])
                        # birth_day = datetime.datetime(*xlrd.xldate_as_tuple(row[4], book.datemode))
                        # hire_day = datetime.datetime(*xlrd.xldate_as_tuple(row[5], book.datemode))

                        employee = EmployeeForm(data={
                            'first_name': str(row[1]),
                            'last_name': str(row[2]),
                            'cin_code': str(row[3]),

                        })
                        if employee.is_valid():
                            employee.save()
                            valid = valid + 1
                        else:
                            print("not valid")
                            invalid = invalid + 1
                            for se in employee:
                                if se.errors:
                                    errors.append(se.errors)
                    except BusinessEntity.DoesNotExist:
                        invalid = invalid + 1
                        errors.append("Business unit does not exist.")
                    # except Level.DoesNotExist:
                    #     invalid = invalid + 1
                    #     errors.append("Level Study does not exist.")
                    # except Degree.DoesNotExist:
                    #     invalid = invalid + 1
                    #     errors.append("Degree Study does not exist.")
                    except Exception as detail:
                        invalid = invalid + 1
                        errors.append(detail)

                    try:
                        list.append({
                            'first_name': str(row[1]),
                            'last_name': str(row[2]),
                            'cin_code': str(row[3]),
                            'birth_day': str(row[4]),  # str(row[4]),  #
                            'hire_day': str(row[5]),  # str(row[5]),  #
                            'email': str(row[6]),
                            'cnss_code': str(row[7]),
                            'experience_years_number': str(row[8]),
                            'level_study': str(row[9]),
                            'degrees_study': str(row[10]),
                            'bu': str(row[11]),
                            'errors': errors
                        })
                    except Exception as detail:
                        list.append({
                            'errors': errors
                        })
                        invalid = invalid + 1
                        errors.append(detail)

        if data.name.endswith('.csv'):  # if the file is csv
            print("--------------------------------------------")
            file_data = data.read().decode("utf-8")  # read file and decode it ti utf-8
            lines = file_data.split("\n")  # split file by return
            print(len(lines))
            if len(lines) == 1 or len(lines) == 0:
                messages.info(request, "no rows found")
                return redirect('employee.import_employee_index')

            print("--------------------------------------------")

            pass

        if invalid == 0:
            messages.info(request, str(valid) + " row(s) inserted, " + str(invalid) + " row(s) invalid")
            return redirect('employee.index')
        else:
            context = {
                'list': list
            }
            return render(request, 'employee/export-errors.html', context)

    context = {
        'form': form
    }
    return render(request, 'employee/export-form.html', context)
