from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.urls import path
from django.conf.urls.static import static

from django.conf import settings
from . import views

urlpatterns = [
    path('', views.homepage, name = "frontpage"),
    path('login/', views.login_user, name = "login"),
    path('logout/', views.logout_user, name = "logout"),
    path('register/', views.register_user, name = "register"),
    path("employee/", views.showjobs, name = "employee"),
]
if(settings.DEBUG):
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
