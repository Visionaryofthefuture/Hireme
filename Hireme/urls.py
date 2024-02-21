from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.urls import path
from django.conf.urls.static import static
from jobs.views import *

from django.conf import settings
from . import views
from userprofile.views import *

urlpatterns = [
    path('', views.homepage, name = "frontpage"), # default page
    path('login/', views.login_user, name = "login"), #login page
    path('logout/', views.logout_user, name = "logout"), #logout user
    path('register/', views.register_user, name = "register"), #register form
    path("employee/", views.detailed_job, name = "employee"), #  shows all the jobs 
    path('addjob/', add_job, name = "addjob"), # form for adding jobs by recruiter
    path('dashboard/', dashboard, name = "dashboard"), #dashboard
    path('detailedjob/', job_detail, name = "detailedjob"),
]

if(settings.DEBUG):
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)