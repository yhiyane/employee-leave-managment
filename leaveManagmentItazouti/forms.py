from django import forms
from django.forms import ModelForm

from .models import *


class employeeForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Prenom", "class": "form-control"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Nom", "class": "form-control"}))
    cin_code = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "CIN", "class": "form-control"}))
    birth_date = forms.DateField(widget=forms.TextInput(attrs={"placeholder": "Date naissance", "class":"form-control", "type":"date"}))
    hire_date = forms.DateField(widget=forms.TextInput(attrs={"placeholder": "Date d'embauche", "class": "form-control", "type":"date"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "Email", "class": "form-control"}))
    cnss_code = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "CNSS", "class": "form-control"}))
    experience_years_number = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Experience", "class": "form-control"}))
    leave_days_number = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder": "Congé", "class": "form-control"}))
    manager = forms.ModelChoiceField(queryset=Employee.objects.filter(isManager=True), widget=forms.Select(attrs={"placeholder": "manager", "class": "form-control"}))
    position = forms.ModelChoiceField(queryset=Position.objects.all(), widget=forms.Select(attrs={"placeholder": "Fonction", "class": "form-control"}))
    team = forms.ModelMultipleChoiceField(queryset=Team.objects.all(), widget=forms.SelectMultiple(attrs={"placeholder": "Team", "class": "form-control"}))
    resignation_date = forms.DateField(widget=forms.TextInput(attrs={"placeholder": "Date démission", "class": "form-control", "type": "date"}))
    isManager = forms.CheckboxInput

    class Meta:
        model = Employee
        fields = [
            'first_name','last_name','cin_code','birth_date','hire_date','email','cnss_code','experience_years_number','leave_days_number',
            'manager','position','team','resignation_date','isManager'
        ]

    def __init__(self, *args, **kwargs):
        super(employeeForm, self).__init__(*args, **kwargs)
        self.fields['resignation_date'].required = False


class teamForm(forms.ModelForm):
    team_code = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Code", "class": "form-control"}))
    libelle = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Libelle", "class": "form-control"}))

    class Meta:
        model = Team
        fields = [
            'team_code','libelle'
        ]


class positionForm(forms.ModelForm):
    position_code = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Code", "class": "form-control"}))
    libelle = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Libelle", "class": "form-control"}))

    class Meta:
        model = Position
        fields = [
            'position_code','libelle'
        ]


class beForm(forms.ModelForm):
    be_Code = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Code", "class": "form-control"}))
    libelle = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Libelle", "class": "form-control"}))

    class Meta:
        model = BusinessEntity
        fields = [
            'be_Code','libelle'
        ]


class leaveRequestForm(forms.ModelForm):
    leave_request_code = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Code", "class": "form-control"}))
    start_date = forms.DateTimeField(widget=forms.TextInput(attrs={"placeholder": "Date démission", "class": "form-control", "type":"date"}))
    end_date = forms.DateTimeField(widget=forms.TextInput(attrs={"placeholder": "Date démission", "class": "form-control", "type":"date" }))
    reason = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Code", "class": "form-control"}))
    status = forms.ChoiceField(choices=STATUS, widget=forms.Select(attrs={"placeholder": "status", "class": "form-control"}))
    employee = forms.ModelChoiceField(queryset=Employee.objects.all(), widget=forms.Select(attrs={"placeholder": "Fonction", "class": "form-control"}))
    manager = forms.ModelChoiceField(queryset=Employee.objects.filter(isManager=True), widget=forms.Select(attrs={"placeholder": "manager", "class": "form-control"}))

    class Meta:
        model = LeaveRequest
        fields = [
            'leave_request_code','start_date', 'end_date', 'reason', 'status', 'employee', 'manager'
        ]
