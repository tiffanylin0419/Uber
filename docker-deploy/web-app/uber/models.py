from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


VEHICLES = [
        ('All', 'All'),
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Truck', 'Truck'),
        ('Minivan', 'Minivan'),
]

NUM=[(1,"1"),(2,"2"),(3,"3"),(4,"4"),(5,"5"),(6,"6"),(7,"7"),(8,"8"),]


class DriverInfo(models.Model):
    driver= models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    maximum_number_of_passenger=models.IntegerField(default=1,choices=NUM)
    vehicle_type= models.CharField(max_length=10,default="Sedan",choices=VEHICLES[1:])
    license_plate= models.CharField(max_length=20,default="")
    def __str__(self):
        return self.license_plate


class Ride(models.Model):
    date_published = models.DateTimeField()
    address = models.CharField(max_length=50,default="")
    arrival_time=models.DateTimeField()
    number_of_passengers=models.IntegerField(default=1,choices=NUM)
    owner= models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    can_be_shared=models.BooleanField(default=False)
    vehicle_type= models.CharField(max_length=10,default="All",choices=VEHICLES)#op
    special_request=models.CharField(max_length=100, blank=True, null = True, default="")#op
    isConfirmed=models.BooleanField(default=False)
    isComplete=models.BooleanField(default=False)
    driver= models.ForeignKey(DriverInfo, on_delete=models.CASCADE, null=True, default=None)
    #sharer = models.ManyToManyField(User, default = None, blank=True, related_name ='sharer')
    #capacity = models.IntegerField(default = 1)

    def __str__(self):
        return self.address

class Sharer(models.Model):
    sharer= models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    ride= models.ForeignKey(Ride, on_delete=models.CASCADE, null=True, default=None)
    number_of_passengers=models.IntegerField(default=1,choices=NUM)

