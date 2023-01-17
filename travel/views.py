from django.shortcuts import render
from django.contrib import messages
from django.core.serializers import serialize
from .forms import LocationForm,DistanceForm,TripForm
from django.contrib.auth.decorators import login_required
from .decorators import *
import json
from django.http import JsonResponse
from .models import Distance,Location
from vehicle.models import Vehicle

@login_required(login_url='/login')
@allowed_users(['enduser'])
def book_trip(request):
    return 

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

@login_required(login_url='/login')
@allowed_users(['admin','enduser'])
def book_trip(request):
    form = TripForm()
    place = Distance.objects.values_list('pfrom',flat=True).distinct()
    print(place)
    place = tuple(place)
    print(place)
    vehicles = Vehicle.objects.filter(intrip = False)
    if request.method == "POST":
        form = TripForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return HttpResponse('Booked Trip Successfully')
        else:
            return HttpResponse(form.errors)
    return render(request,'book_trip.html',{'form':form,'places':place,'vehicles':vehicles})

def getdistance(request,frm,to):
    try:
        dist = Distance.objects.get(pfrom=frm,pto=to)
        return JsonResponse({'distance':dist.distance})
    except:
        return JsonResponse({'message':'no distance'})
def getvehicleprice(request,regno):
    try:
        price = Vehicle.objects.get(vregister_no = regno)
        return JsonResponse({'cost':price.cost})
    except:
        return JsonResponse({'message':'not found'})
def getloacation(reqeuest,frm):
    data = Distance.objects.filter(pfrom = frm)
    json_data = serialize('json',data)
    json_data = json.loads(json_data)
    return JsonResponse({'data':json_data})