from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name = 'userprofile', on_delete = models.CASCADE)
    is_recruiter = models.BooleanField(default = False)
    is_seeker = models.BooleanField(default = True)

    def __str__(self):
        return self.user.username

User.Userprofile = property(lambda u:Userprofile.objects.get_or_create(user = u)[0])