from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Userprofile
# Create your views here.

@login_required
def dashboard(request):
    return render(request, "user/dashboard.html", {"userprofile": request.user.Userprofile})