from django import forms
from .models import Employer

class Employerlogin(forms.ModelForm):
    class Meta:
        models = Employer
        fields =['Name', 'CompanyName', 'Job Position', 'Email', 'Password']
    