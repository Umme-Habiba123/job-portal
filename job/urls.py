from django.urls import path 
from .views import *

urlpatterns = [
    path('', home , name='home'),
    path('login', user_login, name='login'),
    path('logout', user_logout, name='logout'),
    path('registerform', register, name='register'),
    path('jobpost', jobpost, name='jobpost'),
    path('recruiter/dashboard', recruiter_dashboard, name='recruiter_dashboard'),
]
