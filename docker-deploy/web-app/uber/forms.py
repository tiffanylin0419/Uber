from django import forms
from django.forms import ModelForm
from .models import Ride,DriverInfo
from datetime import datetime, timedelta, tzinfo

VEHICLES = [
        ('All', 'All'),
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Truck', 'Truck'),
        ('Minivan', 'Minivan'),
]

NUM=[(1,"1"),(2,"2"),(3,"3"),(4,"4"),(5,"5"),(6,"6"),(7,"7"),(8,"8"),]

from django.contrib.auth.models import User

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'
    
class RequestForm(forms.Form):
    address = forms.CharField(max_length=50)
    # time
    arrival_time = forms.DateTimeField(
        label = 'Earliest Time',
        input_formats = ['%Y-%m-%dT%H:%M'],
        widget = DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'})
        )
    number_of_passengers= forms.ChoiceField(choices=NUM)
    can_be_shared = forms.BooleanField(required=False)
    vehicle_type = forms.ChoiceField(choices=VEHICLES)
    special_request = forms.CharField(max_length=100,required=False)

class DriverForm(forms.Form):
    maximum_number_of_passenger=forms.ChoiceField(choices=NUM)
    vehicle_type = forms.ChoiceField(choices=VEHICLES[1:])
    license_plate= forms.CharField(max_length=20)

	
class RequestUpdateForm(forms.ModelForm):
    class Meta:
        model = Ride
        exclude = ('date_published','owner','isConfirmed','isComplete','driver','license_plate','sharer')

class DriverUpdateForm(forms.ModelForm):
    class Meta:
        model = DriverInfo
        exclude = ('driver',)

    
class SharerSpecifyForm(forms.Form):
    address = forms.CharField(max_length=50)
    earliest_arrival_time = forms.DateTimeField(
        label = 'Earliest Time',
        input_formats = ['%Y-%m-%dT%H:%M'],
        widget = DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'})
        )
    
    latest_arrival_time = forms.DateTimeField(
        label = 'Latest Time',
        input_formats = ['%Y-%m-%dT%H:%M'],
        widget = DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'})
        )
    number_of_passengers = forms.ChoiceField(choices=NUM)