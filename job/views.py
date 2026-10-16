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
      

@login_required(login_url='login')       
def recruiter_dashboard(request):
    jobs=Job.objects.filter(
        recruiter=request.user
    ).order_by('-created_at')
    
    return render(request, 'recruiterDashboard.html',{
        'jobs':jobs
    })
    
    
def update_job(request, id):
    job=Job.objects.get(id=id, recruiter=request.user)
    
    if request.method=='POST':
       form =JobForm(request.POST, instance=job)
    
       if form.is_valid():
           form.save()
           return redirect('recruiter_dashboard')
    
    else:
        form=JobForm(instance=job)
    
    
    return render(request, 'updateJob.html',{
        'form':form
    })
    
    
def delete_job(request, id):
    job=Job.objects.get(id=id, recruiter=request.user)
    
    if request.method=='POST':
        job.delete()
        return redirect('recruiter_dashboard')
    
    return render(request, 'recruiterDashboard.html')


def job_list(request):
    jobs=Job.objects.all().order_by('-created_at')
    
    search_query=request.GET.get('title','')
     
    if search_query:
         jobs=jobs.filter(title__icontains=search_query)
    
    return render(request, 'job_list.html',{
        'jobs':jobs,
        'search_query': search_query,
        
    })
    
def job_details(request, id):
    job=Job.objects.get(id=id)
    
    return render(request, 'job_details.html',{
        'job':job
    })