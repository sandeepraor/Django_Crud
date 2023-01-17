from django.db import models
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from user.models import UserDetails
from vehicle.models import Vehicle
import datetime
class Location(models.Model):
    pfrom = models.CharField('from',primary_key=True,max_length=20)
    class Meta:
        db_table = 'locations'

class Distance(models.Model):
    pfrom  = models.ForeignKey(Location,on_delete=models.CASCADE)
    pto = models.ForeignKey(Location,on_delete=models.CASCADE,related_name='to')
    distance = models.IntegerField('distance(in kms)')
    def clean(self):
        if self.pfrom ==self.pto:
            raise ValidationError('From and To cannot be same')
    class Meta:
        db_table = 'distances'

class BookTrip(models.Model):
    trip_id = models.AutoField('trip_id',primary_key=True)
    from_loc = models.CharField(max_length=30)
    to_loc = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    # retdate = models.DateField()
    vehicle = models.OneToOneField(Vehicle,on_delete=models.SET_DEFAULT , default='No vehicle Selected')
    amount = models.IntegerField(default=0)
    def clean(self):
        if self.from_loc == self.to_loc:
            raise ValidationError('From and To cannot be same')
            