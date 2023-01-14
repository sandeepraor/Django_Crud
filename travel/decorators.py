from django.http import HttpResponse
import functools
from django.contrib import messages
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func

def verification_required(view_func, verification_url="accounts:activate_email"):
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_active:
            return view_func(request, *args, **kwargs)
        messages.info(request, "Email verification required")
        print("You need to be logged out")
        return redirect(verification_url)  
    return wrapper

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            if(group in allowed_roles):
                 return view_func (request,*args,**kwargs) 
            else:
                return HttpResponse("Not Authorised")     
        return wrapper_func
    return decorator