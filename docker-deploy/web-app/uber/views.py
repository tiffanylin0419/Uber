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


def requestRide(request):
    form = forms.RequestForm(request.POST or None)
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

def registration(request):
    form = forms.DriverForm(request.POST or None)
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


def personal(request):
    persons=DriverInfo.objects.filter(driver=request.user)
    if persons:
        person=persons[0]
        return render(request, 'uber/personal.html', locals())
    else:
        return render(request, 'home.html')

def personUpdate(request):
    person=DriverInfo.objects.get(driver=request.user)
    form = forms.DriverUpdateForm(request.POST or None,instance=person)
    if form.is_valid():
        form.save()
        return render(request, 'home.html')
    return render(request, 'uber/personUpdate.html', locals())

def myrides(request):
    data1=Ride.objects.filter(owner=request.user ,isConfirmed=False)
    data2=Ride.objects.filter(owner=request.user ,isConfirmed=True,isComplete=False)
    data3=Ride.objects.filter(owner=request.user ,isComplete=True)

    return render(request, 'uber/myrides.html', locals())

def view(request,ride_id):
    ride=Ride.objects.get(pk=ride_id)
    return render(request, 'uber/view.html', locals())

def update(request,ride_id):
    ride=Ride.objects.get(pk=ride_id)
    form = forms.RequestUpdateForm(request.POST or None,instance=ride)
    if form.is_valid():
        form.save()
        return render(request, 'home.html')
    return render(request, 'uber/update.html', locals())



def driver_search(request):
    
    return HttpResponse("Search for a ride")