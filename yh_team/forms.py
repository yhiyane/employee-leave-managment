from django import forms

from leaveManagementApp.models import Team


# create a Django Form class to generate Business unit form
class TeamForm(forms.ModelForm):
    # forms.ModelForm it will build a form, along with the appropriate fields and their attributes, from a Model class.

    class Meta:
        model = Team  # add the model class

        # declare fields to show in our form
        fields = [
            'team_code',
            'libelle',
        ]

    def __init__(self, *args, **kwargs):
        super(TeamForm, self).__init__(*args, **kwargs)  # call the super constructor for the Form class to override it
        self.fields['libelle'].widget.attrs.update(
            {'class': 'materialize-textarea'})  # add materialize-textarea class to description input
