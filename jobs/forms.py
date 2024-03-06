from . models import Jobs, Application
from django import forms

class AddjobForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = ['role', 'short_desc','long_desc', 'company_name', 'logo', 'category', 'Location']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['content', 'experience']