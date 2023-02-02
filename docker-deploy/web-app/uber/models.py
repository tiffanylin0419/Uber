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
    owner= models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    #sharer_id
    can_be_shared=models.BooleanField(default=False)
    vehicle_type= models.CharField(max_length=50,default="a")#op
    #driver_id
    #isConfirmed
    special_request=models.CharField(max_length=100, blank=True, null = True, default="")#op

    
    def __str__(self):
        return self.address
    #def was_published_recently(self):
    #    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


'''
class DriverInfo(models.Model):
    user_id
    maximum_number_of_passenger
    vehicle_type
    license plate

'''
'''
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        
'''