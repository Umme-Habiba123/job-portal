from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout,get_user_model
from django.contrib.auth.decorators import login_required
from  .forms import *

# Create your views here.

User=get_user_model()

@login_required(login_url='login')

def home(request):
    jobs=Job.objects.all().order_by('created_at')
    return render(request,'home.html',{
       'jobs': jobs   
    }  
    )

def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
             password=form.cleaned_data.get('password1')
             
             user=form.save(commit=False)
             user.set_password(password)
             user.save()
             return redirect('login')
    else:
        form=RegisterForm()
            
    return render(request, 'registerform.html',{
        'form':form
    })


def user_login(request):
    
    if request.method == 'POST':
        form=LoginForm(request, data=request.POST)
        
        if form.is_valid():
            
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            
            user=authenticate(request,username=username, password=password)
            
            if user:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or pass')
    else:
        form=LoginForm()
    
    return render(request, 'login.html',{
        'form':form
    })


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def jobpost(request):
    if request.method=='POST':
        form=JobForm(request.POST)
        
        if form.is_valid():
            job=form.save(commit=False)
            job.recruiter=request.user
            job.save()
            return redirect('home')
    else:
        form=JobForm()
        
    return render(request, 'jobpost.html', {
              'form' : form  
       })   
      
        
def recruiter_dashboard(request):
    jobs=job.objects.filter(
        recruiter=recruiter.user
    ).order_by('created_at')
    
    return render(request, 'recruiter_dashboard.html',{
        'jobs':jobs
    })