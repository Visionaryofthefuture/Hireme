from django.shortcuts import render
from django.http import HttpResponse
from .models import Employer
from django.contrib.auth import login,logout

# Create your views here.


def homepage(request):
    return render(request, "aboutus.html")

def login(request):
    print(request.POST.get("username"))
    return render(request, "forms.html")