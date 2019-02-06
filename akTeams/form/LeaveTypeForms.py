from django import forms
from leaveManagementApp.models import LeaveType

class LeaveTypeForm(forms.ModelForm):

    class Meta:
        model = LeaveType

        fields = [
            'LeaveTypeCode',
            'libelle',
            'daysNumber',
        ]



    def __init__(self, *args, **kwargs):
            super(LeaveTypeForm, self).__init__(*args, **kwargs)

            for visible in self.fields:
                self.fields[visible].widget.attrs.update({'class': 'form-control','pachelor':visible})


