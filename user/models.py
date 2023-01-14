from django.db import models
from django.contrib.auth.models import User

User._meta.get_field('email')._unique = True
class UserDetails(models.Model):
    email = models.OneToOneField(User , on_delete=models.CASCADE , default="NOT Provided",unique=True)
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=1)
    address = models.CharField(max_length=100)
    addhar = models.CharField(max_length=14)

    class Meta:
        db_table = 'user_detail'
