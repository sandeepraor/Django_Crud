from django.db import models
from employee.models import Employee
# Create your models here.
class Vehicle(models.Model):
    employee = models.OneToOneField(Employee , on_delete=models.SET_NULL , null=True)
    vname = models.CharField(max_length=20)
    vregister_no = models.CharField(max_length=20,primary_key=True , default="Not  mentioned")
    vmodel = models.CharField(max_length=20, default="Not  mentioned")
    capacity = models.SmallIntegerField(default=4)
    cost = models.PositiveIntegerField(default=14)
    intrip = models.BooleanField(default=False)
    fuel = models.CharField(max_length=20 , default="Not mentioned")
    

    class Meta:
        db_table = "vehicle"