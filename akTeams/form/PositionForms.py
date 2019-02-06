from django import forms
from leaveManagementApp.models import Position

class PositionForm(forms.ModelForm):

    class Meta:
        model = Position

        fields = [
            'position_code',
            'libelle',
        ]

    def __init__(self, *args, **kwargs):
            super(PositionForm, self).__init__(*args, **kwargs)

            for visible in self.fields:
                self.fields[visible].widget.attrs.update({'class': 'form-control'})


