from django.db import models

# Create your models here.
import datetime
from django.utils import timezone


class Ride(models.Model):
    date_published = models.DateTimeField()
    address = models.CharField(max_length=50,default="")
    arrival_date=models.DateField(default=timezone.now)
    number_of_passengers=models.IntegerField(default=1)
    #owner_id=
    #vehicle #(optional)
    #sharer_id
    #canShare
    #driver_id
    #isConfirmed
    #request(optional)

    
    def __str__(self):
        return self.address
    #def was_published_recently(self):
    #    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

'''
class DriverInfo(models.Model):
    user_id
    vehicle
    

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