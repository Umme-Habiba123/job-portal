from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm ,UserCreationForm


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
    
    password1=forms.CharField(label='Password', widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Password'
        }
    ))
    
    password2=forms.CharField(label='Confirm Password', widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Confirm Password'
        }
    ))
    
    usertype=forms.CharField(label='User Type', widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Role'
        }
    ))
    
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
    
