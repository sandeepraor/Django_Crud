from django.db import models
from django.core.exceptions import ValidationError
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