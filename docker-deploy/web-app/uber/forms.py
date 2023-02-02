from django import forms
from .models import Ride


from django.contrib.auth.models import User

class RequestForm(forms.Form):
    address = forms.CharField(max_length=50)
    arrival_date= forms.DateField(widget=forms.SelectDateWidget)
    arrival_time= forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    number_of_passengers= forms.IntegerField()
    can_be_shared = forms.BooleanField(required=False)