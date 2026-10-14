from django.db import models
from django.contrib.auth.models import  AbstractUser


# Create your models here.

class User(AbstractUser):
   USER_TYPE=[
      ('recruiter', 'Recruiter'),
      ('jobseeker', 'Job Seeker'),
   ]
   
   user_type=models.CharField(
      max_length=20,
      choices=USER_TYPE,
      default='jobseeker',
   )

class Recruiter_Profile(models.Model):
   user=models.OneToOneField(User, on_delete=models.CASCADE)
   company_name=models.CharField(max_length=50)
   company_description=models.CharField(max_length=200)
   company_website=models.CharField(max_length=200)
   company_address=models.CharField(max_length=100)
   contact_info=models.CharField(max_length=100)


   def __str__(self):
       return  self.company_name   

class JobSeeker_Profile(models.Model):
   user= models.OneToOneField(User, on_delete=models.CASCADE)
   full_name= models.CharField(max_length=50)
   phone=models.CharField(max_length=20)
   address=models.CharField(max_length=100)
   skills=models.CharField(max_length=100)
   experience=models.CharField(max_length=100)
   resume=models.CharField(max_length=100)
   

   def __str__(self):
       return  self.full_name

