from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import UserDetails


class CreateUserForm(UserCreationForm):

    class Meta:
        model=User
        fields=['username','email','password1','password2']

class UserDetailsForm(ModelForm):
    class Meta:
        model = UserDetails
        fields = ['email','phone' , 'gender' , 'address' , 'addhar']