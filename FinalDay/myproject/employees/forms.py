from django import forms
from .models import Employee
from django.forms.widgets import ClearableFileInput

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'bio', 'department', 'photo']
        required = {
            'department': False,
        }
        widgets = {
            'photo': ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
