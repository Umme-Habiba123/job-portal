from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from  .forms import *

# Create your views here.


@login_required(login_url='login')

def home(request):
    return render(request,'base.html')

def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
             password=form.cleaned_data.get('password1')
             
             user=form.save(commit=True)
             user.set_password(password)
             user.save()
             return redirect('register')
    else:
        form=RegisterForm()
            
    return render(request, 'registerform.html',{
        'form':form
    })

def user_login(request):
    
    if request.method== 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            
            if user:
                login(request, user)
                return redirect('home')
            else:
                user=LoginForm()
    
    return render(request, 'login.html',{
        'form':form
    })


def user_logout(request):
    
    return render(request, 'logout.html')