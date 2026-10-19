from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout,get_user_model
from django.contrib.auth.decorators import login_required
from  .forms import *
from django.contrib import messages
from .models import *

# Create your views here.

User=get_user_model()

@login_required

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
    
@login_required(login_url='login')   
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
    
@login_required(login_url='login')    
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
    
    
    
def apply_job(request, id):
    job=Job.objects.get( id=id)
    
    if request.user.user_type != 'jobseeker':
        return redirect('job_details', id=job.id)
    if Applications.objects.filter(
        job=job,
        jobseeker=request.user
    ).exists():
        messages.info(request, 'You have already applied for this job')
        
    else:
        resume=request.FILES.get('resume')
        
        if not resume:
            messages.error(request, 'Please uploade your resume')
            return render(request,'Apply_job.html',{
                'job':job
            })
        Applications.objects.create(
            job=job,
            jobseeker=request.user,
            resume=resume
        )
        messages.success(request, 'Application submitted successfully')
        
    return redirect('job_details', id=job.id)



@login_required(login_url='login')
def skill_matched_jobs(request):
    if request.user.user_type != 'jobseeker':
        return redirect('home')

    profile = JobSeeker_Profile.objects.filter(
        user=request.user
    ).first()

    matched_jobs = []

    if profile:
        seeker_skills = {
            skill.strip().lower()
            for skill in profile.skills.split(',')
            if skill.strip()
        }

        jobs = Job.objects.all()

        for job in jobs:
            job_skills = {
                skill.strip().lower()
                for skill in job.skills.split(',')
                if skill.strip()
            }

            common_skills = seeker_skills & job_skills

            if common_skills:
                matched_jobs.append({
                    'job': job,
                    'matched_skills': sorted(common_skills),
                    'match_count': len(common_skills),
                    'total_skills': len(job_skills),
                })

    matched_jobs.sort(
        key=lambda item: item['match_count'],
        reverse=True
    )

    return render(
        request,
        'skill_matched_jobs.html',
        {
            'matched_jobs': matched_jobs,
            'profile_missing': profile is None,
        }
    )


@login_required(login_url='login')
def create_jobseeker_profile(request):
    if request.user.user_type != 'jobseeker':
        return redirect('home')

    profile = JobSeeker_Profile.objects.filter(
        user=request.user
    ).first()

    if request.method == 'POST':
        form = JobSeeker_ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            saved_profile = form.save(commit=False)
            saved_profile.user = request.user
            saved_profile.save()
            messages.success(request, 'Profile saved successfully!')
            return redirect('skill_matched_jobs')
    else:
        form = JobSeeker_ProfileForm(instance=profile)

    return render(
        request,
        'jobseeker_profile.html',
        {'form': form}
    )