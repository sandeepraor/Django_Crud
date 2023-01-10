from django.shortcuts import render

# Create your views here
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import UserDetails
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

@login_required
def profile(request):
   if request.user.groups.all()[0].name == 'admin':
      return redirect('/admin-dashboard')
   if request.user.groups.all()[0].name == 'employee':
      return redirect('/employee-dashboard')
   user_detail = UserDetails.objects.filter(email_id = request.user.id)
   print(request.user.groups.all()[0].name)
   if not user_detail:
      profile_bool = False
      print(profile_bool)
      return render(request,'profile.html',{'profile_bool':not profile_bool})
   else : 
      return render(request,'profile.html',{'details' : user_detail.get()})

@login_required
@allowed_users(['enduser','admin'])
def add_user_detail(request):
   if request.method=="POST":
      form = UserDetailsForm(request.POST)
      form.initial = {'email' : request.user.id}
      print(form.errors)
      print(form.cleaned_data)
      if form.is_valid():
         try:
            form.save()
            return redirect('/profile')
         except:
            pass
      else :
         messages.info(request,form.errors)
   form = UserDetailsForm()
   return render(request,'user_details.html',{'form':form})

@login_required
def edit_user_details(request):
   user_details = UserDetails.objects.get(email = request.user.id)
   print(user_details)
   return render(request,'edit_user.html',{'user_details':user_details})

def update_user_details(request):
   user_details = UserDetails.objects.get(email = request.user.id)
   form = UserDetailsForm(request.POST,instance=user_details)
   if form.is_valid():
      form.save()
      return redirect('/profile')
   return render(request,'edit_user.html',{'user_details':user_details})  