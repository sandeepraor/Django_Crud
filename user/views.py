from django.shortcuts import render

# Create your views here
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .decorators import *
from django.contrib.auth.decorators import login_required
from .decorators import *
from .forms import *
from django.contrib.auth.models import Group

# @unauthenticated_user
def loginUser(request):

      if request.method=='POST':
         username=request.POST.get('username') #name in input tag
         password=request.POST.get('password')
         
         user=authenticate(request, username=username, password=password)
         if user is not None:
            login(request,user)
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            if(group =='enduser'):
                 return redirect ('/') 
            elif(group=='employee') :
                 return redirect ('/employee-dashboard') 
            else:
               return redirect('/profile')  
            
            return redirect('/hms')
         else:
            messages.info(request,"Username or Password Incorrect")
            return render(request,'login.html')
         
      context={}
      return render(request,'login.html',context)
  
  

def register(request):
   form=CreateUserForm()
   print(form)
   if (request.method=="POST"):
         form=CreateUserForm(request.POST)
         print(form)
         if form.is_valid():
            user=form.save()
            username =form.cleaned_data.get('username')
            group=Group.objects.get(name='enduser')
            user.groups.add(group)
            messages.success(request,'Account Created Succesfully for '+username)
            return redirect('/profile')
   
   context={'form':form}
   return render(request,'register.html',context)  

def logoutUser(request):
   logout(request)
   return redirect('/') 

def profile(request):
    return render(request,'profile.html')