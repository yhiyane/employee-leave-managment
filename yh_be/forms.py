from django import forms

from leaveManagementApp.models import BusinessEntity


# create a Django Form class to generate Business unit form
class BEForm(forms.ModelForm):
    # forms.ModelForm it will build a form, along with the appropriate fields and their attributes, from a Model class.

    class Meta:
        model = BusinessEntity  # add the model class

        # declare fields to show in our form
        fields = [
            'be_Code',
            'libelle',
        ]

    def __init__(self, *args, **kwargs):
        super(BEForm, self).__init__(*args, **kwargs)  # call the super constructor for the Form class to override it
        self.fields['libelle'].widget.attrs.update(
            {'class': 'materialize-textarea'})  # add materialize-textarea class to description input
