from django.http import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('login/', views.login, name = "login")
]
