from django.shortcuts import render
from django.http import HttpResponse
from .models import Employer
from django.contrib.auth import login,logout

# Create your views here.

def homepage(request):
    return HttpResponse("<h1> Hello Homepage </h1>")

def login(request):
    print(request.POST.get("username"))
    return render(request, "forms.html")