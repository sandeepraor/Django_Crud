from django.shortcuts import render,redirect
from django.contrib import messages
from tsystem.forms import EmployeeForm  , LoginForm ,VehicleForm
from tsystem.models import Employee  ,Vehicle
# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:
                pass
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})  
def edit(request, eid):  
    employee = Employee.objects.get(eid=eid)  
    return render(request,'edit.html', {'employee':employee})  
def update(request, eid):  
    employee = Employee.objects.get(eid=eid)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  
def destroy(request, eid):  
    employee = Employee.objects.get(eid=eid)  
    employee.delete()  
    return redirect("/show")


def user_login(request):
    if request.method =="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return render(request,'message.html', {'error' : False , 'message' : "Added Successfully" ,'links' : [{'olink': "emp" , 'text': "Click" }]})
            except:
                pass
    else :
        form = LoginForm()
    return render(request,'signin.html',{'form' : form})

# Vehicle urls for function
# Add new Vehicle using the primary key

def vehicle_add(request):
    emp = Employee.objects.all()
    if request.method=="POST":
        form = VehicleForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return render(request,'message.html', {'error':False, 'message':'Data added Successfully' , 'links':[{'olink':'vehicle_get/' , 'text':"Click"}]})
            except:
                pass
    else:
        form = VehicleForm()
    return render(request,'vehicle/vehicle_spinner.html',{'employees':emp})
def vehicle_destroy(request,id):
    vehicle = Vehicle.objects.get(id=id)
    vehicle.delete()
    return render(request,'message.html', {'error':False, 'message':'Data Deleted Successfully' , 'links':[{'olink':'vehicle_get/' , 'text':"Click"}]})

def vehicle_get(request):
    vehicle = Vehicle.objects.all()
    return render(request,'vehicle/vehicle_display.html',{'vehicles':vehicle})