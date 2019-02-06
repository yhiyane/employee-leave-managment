# from django import forms
# from akTeams.models import User
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):


    class Meta:
        model = User
        fields = ['username',
                  'password1',
                  'password2',
                  'is_superuser',
                  ]
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['is_superuser'].label = "Admin"
        self.fields['password2'].label = "Confirm"

        for visible in self.fields:
            if visible == 'is_superuser':
                pass
            else:

                self.fields[visible].widget.attrs.update({'class': 'form-control','placeholder': visible})


# #customer user
#
#
# class RegisterForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ('username',)
#
#     def clean_email(self):
#         username = self.cleaned_data.get('username')
#         qs = User.objects.filter(username=username)
#         if qs.exists():
#             raise forms.ValidationError("username is taken")
#         return username
#
#     def clean_password2(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords don't match")
#         return password2
