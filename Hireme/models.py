from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator

# Create your models here.
class User(models.Model):
    username = models.CharField(default = '', max_length = 255, unique = True)
    email = models.EmailField(default = "", null = False, blank = False, unique = True)
    resume = models.FileField(default = None, upload_to="media", validators= [FileExtensionValidator(["pdf"])])

    def __str__(self):
        return self.username



class Employer(User):
    company_name = models.CharField(default = '', max_length = 23)
