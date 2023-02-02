from django import forms
from .models import Ride

class RequestForm(forms.Form):
    model=Ride
    address = forms.CharField(max_length=50)
    arrival_date= forms.DateField(widget=forms.SelectDateWidget)#input_formats=['%Y-%m-%d'])
    number_of_passengers= forms.IntegerField()