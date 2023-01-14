from django.shortcuts import render , redirect
from .models import Vehicle
from employee.models import Employee
from .forms import VehicleForm
from .decorators import allowed_users
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
@allowed_users(['admin'])
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

def vehicle_edit(request,id):
    vehicle_data = Vehicle.objects.get(vregister_no = id)
    employees = Employee.objects.all()
    return render(request,'vehicle_update.html',{'vehicle':vehicle_data,'employees':employees})
def vehicle_update(request,id):
    vehicle_data = Vehicle.objects.get(vregister_no = id)
    employee = Employee.objects.all()
    form = VehicleForm(request.POST,instance=vehicle_data)
    if form.is_valid():
        form.save()
        return redirect('/vehicle_get')
    return render(request,'vehicle_update.html',{'vehicle':vehicle_data,'employees':employee})