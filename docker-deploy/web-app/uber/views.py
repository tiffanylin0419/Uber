from . import forms
from .models import Ride,DriverInfo
from django.shortcuts import render
from django.utils import timezone

# Create your views here.

#add
from django.http import HttpResponse

from django.urls import reverse_lazy
from django.views import generic

def index(request):#delete
    return HttpResponse("Hello, world. You're at the polls index.")

def registration(request):
    form = forms.DriverForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            r = DriverInfo(driver=request.user, 
                    maximum_number_of_passenger=form.cleaned_data['maximum_number_of_passenger'],
                    vehicle_type=form.cleaned_data['vehicle_type'],
                    license_plate=form.cleaned_data['license_plate'],
                    )
            r.save()
            return render(request, 'home.html')
    return render(request, 'uber/request.html', locals())

def view(request):
    form = forms.DriverForm(request.POST)


def requestRide(request):
    form = forms.RequestForm(request.POST)
    #fields = ['address']
    if request.method == 'POST':
        if form.is_valid():
            print("form is valid")
            r = Ride(address=form.cleaned_data['address'], 
                    date_published=timezone.now(),
                    arrival_date = form.cleaned_data['arrival_date'],
                    arrival_time = form.cleaned_data['arrival_time'],
                    number_of_passengers=form.cleaned_data['number_of_passengers'],
                    owner=request.user, 
                    can_be_shared=form.cleaned_data['can_be_shared'],
                    special_request=form.cleaned_data['special_request'],
                    )
            r.save()
            return render(request, 'home.html')
    return render(request, 'uber/request.html', locals())


def edit(request):
    return HttpResponse("Edit")

def myrides(request):
    return render(request, 'uber/myrides.html')

def search(request):
    return HttpResponse("Search for a ride")