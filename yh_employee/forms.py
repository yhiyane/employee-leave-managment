from django import forms
from django.core.validators import FileExtensionValidator

from leaveManagementApp.models import Employee, BusinessEntity, Team

# create a Django Form class to generate Employee form
from yh_employee.models import Document


class EmployeeForm(forms.ModelForm):
    be = forms.ModelChoiceField(queryset=BusinessEntity.objects.all(), empty_label='Select Business unit')


    class Meta:
        model = Employee
        fields = [
            'first_name',
            'last_name',
            'cin_code',
            'birth_date',
            'hire_date',
            'email',
            'cnss_code',
            'be',
            'position',
            'experience_years_number',
            'manager',
            'teams',
        ]

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['be'].label = "Business Entity"  # modify label fot the bu field
        self.fields['birth_date'].widget.attrs.update(
            {'class': 'datepicker'})  # add datepicker class to birth_date field
        self.fields['hire_date'].widget.attrs.update({'class': 'datepicker'})  # add datepicker class to hire_date field
        self.fields['position'].label = "Position"

    def clean_birth_date(self):
        date = self.cleaned_data['birth_date']
        if date > date.today():  # check if the birth day is greater than the current date
            raise forms.ValidationError("The date cannot be in the future!")
        return date


# create a Django Form class to generate Export Form
class ExportForm(forms.Form):
    attached_piece = forms.FileField(widget=forms.FileInput(
        attrs={
            'accept': '.xls,.csv',
            'name': 'attached_piece',
            'class': 'file-input'
        },
    ),
        validators=[FileExtensionValidator(['xls', 'csv'])]  # valid extensions
    )

    fields = [
        'attached_piece'
    ]
