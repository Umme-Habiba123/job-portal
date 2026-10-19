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
   resume=models.FileField(upload_to='resumes/')
   

   def __str__(self):
       return  self.full_name

class Job(models.Model):
   recruiter=models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')
   title=models.CharField(max_length=200)
   vacancy=models.CharField(max_length=20)
   category=models.CharField(max_length=200)
   jobdescription=models.CharField(max_length=200)
   skills=models.CharField(max_length=300)
   created_at=models.DateTimeField(auto_now_add=True)
   
   def __str__(self):
      return self.title
   

class Applications(models.Model):
   STATUS_CHOICES=[
      ('pending', 'Pending'),
      ('shortlisted', 'Shortlisted'),
      ('rijected', 'Rijected'),
   ]
   
   job=models.ForeignKey(
      Job, on_delete=models.CASCADE,related_name='applications'
   )
   jobseeker=models.ForeignKey(User, on_delete=models.CASCADE,related_name='job_applications')
   
   applied_at=models.DateTimeField(auto_now_add=True)
   resume = models.FileField(
    upload_to='application_resumes/',
    blank=True,
    null=True
    )
   status=models.CharField(max_length=20,        choices=STATUS_CHOICES, default='pending')
   
   class Meta:
      unique_together=('job', 'jobseeker')
      
   def __str__(self):
      return f'{self.jobseeker.username}-{self.job.title}'