from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm
from django.urls import reverse
from userprofile.models import Userprofile
from jobs.models import Jobs
from django.shortcuts import render, redirect
# Create your views here.


def homepage(request):
    if(request.user.is_authenticated == True):
           jobs1 = Jobs.objects.all()
           to_show = jobs1[0:]
           return render(request, "job seeker/jobs.html", {'jobs': to_show})
    return render(request, "user/aboutus.html")
    



def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username is not None and password is not None:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Login succes")
                return redirect(reverse("employee"))
            else:
                messages.error(request, "Sorry, couldn't login. Please check your credentials.")
        else:
            messages.error(request, "Username and password are required.")
            
    return render(request, "user/forms.html")


def logout_user(request):
    logout(request)
    messages.success(request, ("successfully logged out"))
    return redirect("frontpage")


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            accounttype = request.POST.get('account_type', 'jobseeker')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            if accounttype == "recruiter":
                userprofile = Userprofile.objects.create(user=user, is_recruiter=True)
            elif accounttype == "jobseeker":
                userprofile = Userprofile.objects.create(user=user, is_seeker=True)

            login(request, user)
            messages.success(request, "Successfully registered")
            print(username, password)
            return redirect('employee')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    print(f"Error in field {field}: {error}")
            return redirect("register")
    else:
        return render(request, 'user/register.html', {'form': form})

def detailed_job(request):
    jobs1 = Jobs.objects.all()
    to_show = jobs1[0:]
    return render(request, "job seeker/jobs.html", {'jobs': to_show})
    
    