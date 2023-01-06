
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import EmployeeForm 
from .models import Employee
from .decorators import *
from django.contrib.auth.decorators import login_required
#Load home page
def homepage(request):
    return render(request,'home_page.html')


# Create your views here.  
def emp(request):  
    employee=Employee.objects.last()
    if request.method == "POST":  
        form = EmployeeForm(request.POST,request.FILES)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:
                pass
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form , 'id':employee.eid+1}) 

@login_required(login_url='/login')
@allowed_users(['employee','admin'])
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

def admindashboard(request):
    return render(request,'admin_dashboard.html')


def employeedashboard(request):
    return render(request,'employee_dashboard.html')
