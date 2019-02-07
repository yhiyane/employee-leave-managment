from django import forms
from .models import LeaveRequest,Notifications


class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = [
            'leave_request_code',
            'start_date',
            'start_time',
            'end_date',
            'end_time',
            'create_date',
            'status',
            'motif',
            'reason',
            'employee',
            'manager'
        ]

    def __init__(self, *args, **kwargs):
        super(LeaveRequestForm, self).__init__(*args, **kwargs)
        self.fields['reason'].widget.attrs.update({"style": "height: 120px;"})
        self.fields['motif'].widget.attrs.update({"style": "margin-top: 20px;"})
        for visible in self.fields:
            self.fields[visible].widget.attrs.update({'class': 'input--style-4'})

