from django import forms

from leaveManagementApp.models import LeaveRequest


# create a Django Form class to generate Business unit form
class LeaveRequestForm(forms.ModelForm):
    # forms.ModelForm it will build a form, along with the appropriate fields and their attributes, from a Model class.

    class Meta:
        model = LeaveRequest  # add the model class

        # declare fields to show in our form
        fields = [
            'leave_request_code',
            'employee',
            'manager',
            'start_date',
            'start_time',
            'end_date',
            'end_time',
            'reason',
            'status',

        ]

    def __init__(self, *args, **kwargs):
        super(LeaveRequestForm, self).__init__(*args, **kwargs)  # call the super constructor for the Form class to override it
        self.fields['leave_request_code'].widget.attrs.update({'class': 'materialize-textarea'})  # add materialize-textarea class to description input
        self.fields['start_date'].widget.attrs.update({'class': 'datepicker'})  # add datepicker class to birth_date field
        self.fields['end_date'].widget.attrs.update({'class': 'datepicker'})  # add datepicker class to hire_date field



