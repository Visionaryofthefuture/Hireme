from django import forms

class Employerform(forms.Form):
    name = forms.CharField(max_length= 25)
    email = forms.EmailField()
    company = forms.CharField()
    