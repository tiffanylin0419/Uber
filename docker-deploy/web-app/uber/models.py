from django.db import models

# Create your models here.
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

class Ride(models.Model):
    date_published = models.DateTimeField()
    address = models.CharField(max_length=50,default="")
    arrival_date=models.DateField(default=timezone.now)
    arrival_time=models.TimeField(default=timezone.now)
    number_of_passengers=models.IntegerField(default=1)
    owner= models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner', null=True, default=None)
    can_be_shared=models.BooleanField(default=False)
    vehicle_type= models.CharField(max_length=5,default="All")#op
    special_request=models.CharField(max_length=100, blank=True, null = True, default="")#op
    isConfirmed=models.BooleanField(default=False)
    isComplete=models.BooleanField(default=False)
    driver= models.ForeignKey(User, on_delete=models.CASCADE, related_name='driver', null=True, default=None)
    license_plate= models.CharField(max_length=20, blank=True, null = True, default="")
    #sharer
    #driver



    def __str__(self):
        return self.address
    #def was_published_recently(self):
    #    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class DriverInfo(models.Model):
    driver= models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    maximum_number_of_passenger=models.IntegerField(default=1)
    vehicle_type= models.CharField(max_length=5,default="b")
    license_plate= models.CharField(max_length=20,default="")
    def __str__(self):
        return self.license_plate
