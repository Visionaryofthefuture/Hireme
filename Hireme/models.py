from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(models.Model):
    username = models.CharField(default = '', max_length = 255)
    email = models.EmailField(default = "", null = False, blank = False)
    resume = models.FileField(default = "", upload_to="media")
