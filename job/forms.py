from django import forms
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm ,UserCreationForm

User =get_user_model()


class Recruiter_ProfileForm(forms.ModelForm):
     class Meta:
         model=Recruiter_Profile
         fields= '__all__'
         
         
         
class RegisterForm(UserCreationForm):
    username=forms.CharField(label='Username', widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Enter Login'
        }
    ))
    
    displayname=forms.CharField(label='displayname', widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Display Name'
        }
    ))
    
    email=forms.CharField(label='Email', widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Write Your Email'
        }
    ))
    
    password1=forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Password'
        }
    ))
    
    password2=forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Confirm Password'
        }
    ))
    
    user_type=forms.ChoiceField(label='User Type', choices=[
        ('recruiter','Recruiter'),
        ('jobseeker','Job Seeker'),
        
        ] , 
            widget=forms.Select(
        attrs={
            'class':'form-select',
        }
    ))
    
    class Meta:
        model=User
        fields=['username', 'displayname', 'email','password1', 'password2', 'user_type']
    
class LoginForm(AuthenticationForm):
    
     username=forms.CharField(label='Username', widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Enter Login'
        }
    ))
     
     password=forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Password'
        }
    ))
    

class JobForm(forms.ModelForm):
    class Meta:
        model=Job
        fields=['title', 'vacancy','category','job-description','skills']
        
    #  widget={
    #      'description':forms.Textarea(
    #          attrs={
    #              'rows'=4
    #          }
    #      ),
    #      'skills':forms.Textarea(
    #          attrs={
    #              'rows':2
    #          }
    #      ),
    #  }