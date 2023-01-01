from django.shortcuts import render
from .models import Vehicle
from employee.models import Employee
from .forms import VehicleForm

def vehicle_add(request):
    emp = Employee.objects.all()
    if request.method=="POST":
        form = VehicleForm(request.POST)
        print(form)
        if form.is_valid():
            try:
                print(form)
                form.save()
                return render(request,'message.html', {'error':False, 'message':'Data added Successfully' , 'links':[{'olink':'vehicle_get/' , 'text':"Click"}]})
            except:
                pass
    else:
        form = VehicleForm()
    return render(request,'vehicle_spinner.html',{'employees':emp,'form':form})


def vehicle_destroy(request,id):
    vehicle = Vehicle.objects.get(vregister_no = id)
    vehicle.delete()
    return render(request,'message.html', {'error':False, 'message':'Data Deleted Successfully' , 'links':[{'olink':'vehicle_get/' , 'text':"Click"}]})

def vehicle_get(request):
    vehicle = Vehicle.objects.all()
    return render(request,'vehicle_display.html',{'vehicles':vehicle})
