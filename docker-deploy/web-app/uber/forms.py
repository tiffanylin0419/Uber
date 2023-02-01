from django import forms
from .models import RequestRide

class RequestForm(forms.Form):
    model=RequestRide
    address = forms.CharField(max_length=50)