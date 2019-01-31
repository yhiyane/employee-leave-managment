from django import forms

from leaveManagementApp.models import LeaveRequest


# create a Django Form class to generate Business unit form
class LeaveRequestForm(forms.ModelForm):
    # forms.ModelForm it will build a form, along with the appropriate fields and their attributes, from a Model class.
    half_day = forms.BooleanField(widget=forms.CheckboxInput(), required=False)

    class Meta:
        model = LeaveRequest  # add the model class

        # declare fields to show in our form
        fields = [
            # 'employee',
            'leave_request_code',
            'half_day',
            'half_day_status',
            'start_date',
            'end_date',
            'reason',
            # 'status',

        ]

    def __init__(self, *args, **kwargs):
        self.show_half_day = kwargs.pop('show_half_day', False)
        super(LeaveRequestForm, self).__init__(*args, **kwargs)

        self.fields['leave_request_code'].widget.attrs.update(
            {'class': 'materialize-textarea'})  # add materialize-textarea class to description input
        self.fields['start_date'].widget.attrs.update(
            {'class': 'datepicker'})  # add datepicker class to birth_date field
        self.fields['end_date'].widget.attrs.update({'class': 'datepicker'})  # add datepicker class to hire_date field

        if not self.show_half_day:
            del self.fields['half_day']
        # else:
        #     #self.fields['start_time'].required = False
        #     #self.fields['end_time'].required = False
