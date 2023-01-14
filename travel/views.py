from django.shortcuts import render
from django.contrib import messages
from .forms import LocationForm,DistanceForm
from django.contrib.auth.decorators import login_required
from .decorators import *
from .models import Distance,Location

@login_required(login_url='/login')
@allowed_users(['admin'])
def add_place(request):
    place = Location.objects.all()
    if request.method=="POST":
        place_form = LocationForm(request.POST)
        if place_form.is_valid():
            try:
                place_form.save()
                return redirect('/get_route')
            except:
                pass
    place_form = LocationForm()
    return render(request,'add_place.html',{'place_form':place_form,'places':place})


@login_required(login_url='/login')
@allowed_users(['admin'])  
def all_places_routes(request):
    loc = Location.objects.all()
    route = Distance.objects.all()
    return render(request,'show_routes.html',{ 'locations' : loc ,'routes':route})


@login_required(login_url='/login')
@allowed_users(['admin'])   
def add_fromto(request):
    place_form = DistanceForm(request.POST)
    print(place_form)
    if place_form.is_valid():
        try:
            place_form.save()
            return redirect('/get_route')
        except:
            pass
    return redirect('/get_route')
