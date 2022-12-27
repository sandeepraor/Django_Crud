from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login 
from django.contrib.auth import authenticate, login

from tsystem.forms import EmployeeForm, NewUserForm, RegisterForm  
from tsystem.models import Employee  
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
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")

def index(request):
    return HttpResponse("Hellos world")


# login part 


def login_view(request): 
    if request.method == 'POST':
        usernames = request.POST['username']
        passwords = request.POST['password']
        print(usernames,passwords)
        user = authenticate(request, username=usernames, password=passwords),
        print({"User":user})
        if user is not None:
            login(request, user)
            print(login,user,usernames)
            print("success")
            return redirect('/')
    print(request)
    return render(request, 'login.html')
    
    # register part
def register_request(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'reg.html', {'form': form})
# def login_view(request): 
#     if request == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = register(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             print(login,user,username)
#             print("success")
#             return redirect('/')
#     print("failure")
#     return render(request, 'login.html', {'error': 'Invalid username or password'})


