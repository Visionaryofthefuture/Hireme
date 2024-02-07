from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def homepage(request):
    return render(request, "user/aboutus.html")

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)

        if username is not None and password is not None:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Login succes")
                return redirect("frontpage")
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
    if(request.method == "POST"):
        form = SignUpForm(request.POST)
        if(form.is_valid()):
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)

            messages.success(request, ("Successfully registered"))
            print(username, password)
            return redirect('frontpage')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    print(f"Error in field {field}: {error}")
            return redirect("register")
            
    else:
        return render(request, 'user/register.html', {'form': form})






    
    