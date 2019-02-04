from django import forms
from .models import Employee, Team, BusinessUnit, Position, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class EmployerRegister(forms.Form):
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Enter the first name",
                   "class": "input100"
                   }
        )
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Enter the last name",
                   "class": "input100"
                   }
        )
    )
    cin_code = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Enter the CIN code",
                   "class": "input100"
                   }
        )
    )
    birth_date = forms.DateField(
        input_formats=['%Y-%m-%d'],
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "input100",
                "type": 'date'
            }
        )
    )
    hire_date = forms.DateField(
        input_formats=['%Y-%m-%d'],
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "input100",
                "type": 'date'
            }
        )
    )
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter Employer's Email",
                "class": "input100",
                "type": 'email'
            }
        )
    )
    cnss_code = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Enter the CNSS code",
                   "class": "input100"
                   }
        )
    )
    experience_years_number = forms.IntegerField(
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Enter the experience years",
                   "class": "input100",
                   'type': 'number'
                   }
        )

    )
    bu_choices = [[b.id, b.libelle] for b in BusinessUnit.objects.all()]
    be = forms.ChoiceField(
        required=True,
        widget=forms.Select(
            attrs={
                "class": "input100",
                "style": "border: none;"
            }
        ),
        choices=bu_choices
    )
    position_choice = [[p.id, p.libelle] for p in Position.objects.all()]
    position = forms.ChoiceField(
        required=True,
        widget=forms.Select(
            attrs={
                "class": "input100",
                "style": "border: none;"
            }
        ),
        choices=position_choice
    )
    managers_choice = [[m.id, m.first_name + '  ' + m.last_name] for m in Employee.objects.filter(tag_manager=True)]
    managers = forms.ChoiceField(
        required=False,
        widget=forms.Select(
            attrs={
                "class": "input100",
                "style": "border: none;"
            }
        ),
        choices=managers_choice
    )
    tag_manager = forms.BooleanField(
        required=False
    )
    teams_choices = [[t.id, t.libelle] for t in Team.objects.all()]
    team = forms.MultipleChoiceField(
        required=False,
        widget=forms.SelectMultiple(
            attrs={
                "class": "input100",
            }
        ),
        choices=teams_choices
    )


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'is_superuser'

        ]

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['is_superuser'].widget.attrs.update({"class": "form-check-input", "label": 'sdf'})
        self.fields['username'].widget.attrs.update({"class": "form-control"})
        self.fields['password1'].widget.attrs.update({"class": "form-control"})
        self.fields['password2'].widget.attrs.update({"class": "form-control"})


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        for visible in self.fields:
            self.fields[visible].widget.attrs.update({'class': 'form-control'})

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class EditForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'first_name',
            'last_name',
            'cin_code',
            'birth_date',
            'hire_date',
            'email',
            'cnss_code',
            'experience_years_number',
            'be',
            'positon',
            'manager',
            'team',
        ]

    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)
        self.fields['manager'].queryset = Employee.objects.filter(tag_manager=True)
        for visible in self.fields:
            self.fields[visible].widget.attrs.update({'class': 'form-control'})





class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = [
            'libelle',
        ]

    def __init__(self, *args, **kwargs):
        super(TeamForm, self).__init__(*args, **kwargs)
        for visible in self.fields:
            self.fields[visible].widget.attrs.update(
                {
                    'class': 'form-control',
                    'style': 'width: 89%;',
                    'placeholder': "Enter team's name"

                }
            )


class BUForm(forms.ModelForm):
    class Meta:
        model = BusinessUnit
        fields = [
            'libelle',
        ]

    def __init__(self, *args, **kwargs):
        super(BUForm, self).__init__(*args, **kwargs)
        for visible in self.fields:
            self.fields[visible].widget.attrs.update(
                {
                    'class': 'form-control',
                    'style': 'width: 89%;',
                    'placeholder': "Enter BU name"

                }
            )


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = [
            'libelle',
        ]

    def __init__(self, *args, **kwargs):
        super(PositionForm, self).__init__(*args, **kwargs)
        for visible in self.fields:
            self.fields[visible].widget.attrs.update(
                {
                    'class': 'form-control',
                    'style': 'width: 89%;',
                    'placeholder': "Enter position name"

                }
            )
