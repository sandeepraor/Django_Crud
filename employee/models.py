from django.db import models

class Employee(models.Model):  

    eid = models.AutoField(primary_key=True)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)
    eage = models.SmallIntegerField(default=18)
    eaddhar = models.CharField(max_length=14 , default="Not Mentioned")
    isverified = models.BooleanField(default=False)
    # eimage = models.ImageField(upload_to='images/' , default="Not Provided")

    class Meta:  
        db_table = "employee" 
