from django.db import models
class Employee(models.Model):  

    eid = models.AutoField(primary_key=True)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)  
    class Meta:  
        db_table = "employee"  
class Login(models.Model):
    
    username = models.CharField(max_length=20 , primary_key=True)
    password = models.CharField(max_length=16 )
    class Meta:
        db_table = "login"

class Vehicle(models.Model):
    employee = models.ForeignKey("employee" , on_delete=models.SET_NULL , null=True)
    vname = models.CharField(max_length=20)
    class Meta:
        db_table = "vehicle"