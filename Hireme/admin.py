from django.contrib import admin

# Register your models here.
from . models import *
from .models import User
from .models import Employer

admin.site.register(User)
admin.site.register(Employer)