from django import forms
from django.forms import ModelForm
from .models import EmployeeDeatils

class EmployeeForm(ModelForm):
    class Meta:
        model = EmployeeDeatils
        
        fields = ('name', 'salary', 'id', 'email_id')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
             'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Salary'}),
            'id': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Id'}),
            'email_id': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }



class MyMailForm(forms.Form):
    UserName = forms.CharField(max_length=250)
    Email = forms.EmailField()


    def __str__(self):
        return self.Email