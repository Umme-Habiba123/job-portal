from django.db import models

# Create your models here.

class Recruiter_Profile(models.Model):
   company_name=models.CharField(max_length=50)
   company_description=models.CharField(max_length=200)
   company_website=models.CharField(max_length=200)
   company_address=models.CharField(max_length=100)
   contact_info=models.CharField(max_length=100)
   
   
   def __str__(self):
       return  self.name
    