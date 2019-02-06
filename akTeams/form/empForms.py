from django import forms
from leaveManagementApp.models import Employee


class empForm(forms.ModelForm):
    manager = forms.ModelChoiceField(queryset=Employee.objects.filter(isManager=True))
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
            'experience_years_number',
            'positon',
            'be',
            'manager',
            'isManager',



        ]

    def __init__(self, *args, **kwargs):
            super(empForm, self).__init__(*args, **kwargs)
            self.fields['be'].label = "Business Entity"
            self.fields['birth_date'].widget.attrs.update({'data-provide': 'datepicker'})
            self.fields['hire_date'].widget.attrs.update({'data-provide': 'datepicker'})
            for visible in self.fields:
                if visible == 'isManager' :
                    pass
                else:
                 self.fields[visible].widget.attrs.\
                    update({
                    'class': 'form-control',
                    'placeholder': visible,
                })


