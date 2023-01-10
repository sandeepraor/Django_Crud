from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
    email = models.OneToOneField(User , on_delete=models.SET_DEFAULT , default="NOT Provided",unique=True)
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=1)
    address = models.CharField(max_length=100)
    addhar = models.CharField(max_length=14)

    class Meta:
        db_table = 'user_detail'
