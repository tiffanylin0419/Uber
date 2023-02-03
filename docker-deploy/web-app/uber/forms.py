from django import forms
from django.forms import ModelForm
from .models import Ride,DriverInfo

VEHICLES = [
        ('All', 'All'),
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Truck', 'Truck'),
        ('Minivan', 'Minivan'),
]

NUM=[(1,"1"),(2,"2"),(3,"3"),(4,"4"),(5,"5"),(6,"6"),(7,"7"),(8,"8"),]

from django.contrib.auth.models import User

class RequestForm(forms.Form):
    address = forms.CharField(max_length=50)
    arrival_date= forms.DateField(widget=forms.SelectDateWidget)
    arrival_time= forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
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
        exclude = ('date_published','owner','isConfirmed','isComplete','driver','license_plate')

class DriverUpdateForm(forms.ModelForm):
    class Meta:
        model = DriverInfo
        exclude = ('driver',)
