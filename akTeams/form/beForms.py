from django import forms
from leaveManagementApp.models import BusinessEntity

class BeForm(forms.ModelForm):

    class Meta:
        model = BusinessEntity

        fields = [
            'be_Code',
            'libelle',
        ]



    def __init__(self, *args, **kwargs):
            super(BeForm, self).__init__(*args, **kwargs)

            for visible in self.fields:
                self.fields[visible].widget.attrs.update({'class': 'form-control','pachelor':visible})


