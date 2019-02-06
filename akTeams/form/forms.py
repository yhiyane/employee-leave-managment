from django import forms
from leaveManagementApp.models import Team

class TeamForm(forms.ModelForm):

    class Meta:
        model = Team

        fields = [
            'team_code',
            'libelle',
            'members'


        ]

    def __init__(self, *args, **kwargs):
            super(TeamForm, self).__init__(*args, **kwargs)

            for visible in self.fields:
                self.fields[visible].widget.attrs.update({'class': 'form-control'})


