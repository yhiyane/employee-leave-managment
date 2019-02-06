from django import forms
from leaveManagementApp.models import Employee,Team


class MemberTeamForm(forms.ModelForm):



    class Meta:
        model = Team

        fields = [

            'members',



        ]

    def __init__(self, *args, **kwargs):
            super(MemberTeamForm, self).__init__(*args, **kwargs)
            for visible in self.fields:
                self.fields[visible].widget.attrs.\
                    update({
                    'class': 'form-control',
                })


class MTeamForm(forms.ModelForm):
    teams = forms.ModelChoiceField(queryset=Team.objects.all(), empty_label='Select Team')

    class Meta:
        model = Team

        fields = [
            'teams',
            'members',



        ]

    def __init__(self, *args, **kwargs):
            super(MTeamForm, self).__init__(*args, **kwargs)
            for visible in self.fields:
                self.fields[visible].widget.attrs.\
                    update({
                    'class': 'form-control',
                })


