from django.db import models
from django.contrib.auth.models import  AbstractUser


# Create your models here.

class User(AbstractUser):
   USER_TYPE=[
      {'recruiter', 'Recruiter'},
      {'jobseeker', 'JobSeeker'},
   ]

class Recruiter_Profile(models.Model):
   company_name=models.CharField(max_length=50)
   company_description=models.CharField(max_length=200)
   company_website=models.CharField(max_length=200)
   company_address=models.CharField(max_length=100)
   contact_info=models.CharField(max_length=100)
#    created_by=models.ForeignKey(User, on_delete = models.CASECADE)
   
   def __str__(self):
       return  self.company_name

# class JobSeeker_Profile():