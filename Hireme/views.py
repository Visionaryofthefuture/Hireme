from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login,logout

# Create your views here.

def homepage(request):
    return HttpResponse("<h1> Hello Homepage </h1>")