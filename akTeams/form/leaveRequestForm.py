from django import forms
from leaveManagementApp.models import LeaveRequest
from datetime import date

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest

        fields = [
            'start_date',
            'end_date',
            'reason',
            'leave_type',



        ]

    def __init__(self, *args, **kwargs):
            super(LeaveRequestForm, self).__init__(*args, **kwargs)

            # self.fields['employee'].widget.attrs.update({'class': 'form-control'})
            self.fields['reason'].widget.attrs.update({'class': 'form-control'})
            self.fields['start_date'].initial = date.today()
            self.fields['leave_type'].label = "motifs"
            self.fields['leave_type'].widget.attrs.update({'class': 'form-control'})
            # self.fields['end_date'].widget.attrs.update({'data-provide': 'datepicker'})
            #
            # for visible in self.fields:
            #     self.fields[visible].widget.attrs.\
            #         update({
            #         'class': 'form-control',
            #
            #     })


