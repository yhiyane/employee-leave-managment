from django import forms
from django.contrib.auth.models import User


# create a User Form class to generate User form
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    edit_password = forms.BooleanField(widget=forms.CheckboxInput(), required=False)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'is_superuser',
            'edit_password',
            'password',
            'confirm_password',
        ]

    def __init__(self, *args, **kwargs):
        self.show_edit_password = kwargs.pop('show_edit_password', False)
        super(UserForm, self).__init__(*args, **kwargs)
        # self.fields['description'].widget.attrs.update({'class': 'materialize-textarea'})
        self.fields['is_superuser'].label = "Admin"

        if not self.show_edit_password:
            del self.fields['edit_password']
            self.fields['is_superuser'].widget.attrs['create-form'] = 'yes'
        else:
            self.fields['password'].required = False
            self.fields['confirm_password'].required = False

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        edit_password = self.cleaned_data.get('edit_password')
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        print("-----------------------------------------------")
        print(edit_password)
        print("-----------------------------------------------")

        if edit_password:
            if not bool(password.strip()):
                raise forms.ValidationError(
                    {'password': ["This field is required"]}
                )

            if password != confirm_password:
                raise forms.ValidationError(
                    {'confirm_password': ["Your password and confirmation password do not match"]}
                )
        if edit_password is None:
            if password != confirm_password:
                raise forms.ValidationError(
                    {'confirm_password': ["Your password and confirmation password do not match"]}
                )

        return self.cleaned_data
