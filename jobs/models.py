from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

class Jobs(models.Model):
    
    role  = models.CharField(max_length = 25)
    recruiter = models.ForeignKey(User, related_name = 'jobs', on_delete = models.CASCADE)
    created_at = models.DateField(null = False, blank = False , auto_now_add = True)
    company_name = models.CharField(default = "random ", max_length = 50)
    logo = models.ImageField(default = None,upload_to="companylogos", null = False, validators=[FileExtensionValidator (allowed_extensions=['png', 'jpg', 'jpeg'])])
    category = models.CharField(default = "information technology", max_length = 50)
    Location = models.CharField(default = " ",max_length = 100)
    short_desc = models.TextField(verbose_name='Short Description', null = False, blank = False, max_length = 255)
    long_desc = models.TextField(verbose_name='Long Description', null = False, blank = False, max_length = 255)

    def __str__(self):
        return self.role
    
class Application(models.Model):
    job = models.ForeignKey(Jobs, related_name = "applications", on_delete = models.CASCADE)
    content = models.TextField()
    experience = models.TextField()
    created_by = models.ForeignKey(User, related_name = "applications", on_delete = models.CASCADE)
    created_at = models.DateField(null = False, blank = False , auto_now_add = True)

