from . import forms
from .models import Ride,DriverInfo
from django.shortcuts import render
from django.utils import timezone

from django.db.models import Q
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

def myrides_rider(request):
    data1=Ride.objects.filter(owner=request.user ,isConfirmed=False)
    data2=Ride.objects.filter(owner=request.user ,isConfirmed=True,isComplete=False)
    data3=Ride.objects.filter(owner=request.user ,isComplete=True)

    return render(request, 'uber/myrides_rider.html', locals())

def myrides_driver(request):
    data1=Ride.objects.filter(driver=request.user ,isComplete=False)
    data2=Ride.objects.filter(driver=request.user ,isComplete=True)

    return render(request, 'uber/myrides_driver.html', locals())

def view(request,ride_id):
    ride=Ride.objects.get(pk=ride_id)
    return render(request, 'uber/view.html', locals())

def view_d(request,ride_id):
    ride=Ride.objects.get(pk=ride_id)
    return render(request, 'uber/view_d.html', locals())

def update(request,ride_id):
    ride=Ride.objects.get(pk=ride_id)
    form = forms.RequestUpdateForm(request.POST or None,instance=ride)
    if form.is_valid():
        form.save()
        return render(request, 'home.html')
    return render(request, 'uber/update.html', locals())



def driver_search(request):
    persons=DriverInfo.objects.filter(driver=request.user)
    if persons:
        person=persons[0]
        data=Ride.objects.filter(Q(vehicle_type=person.vehicle_type) | Q(vehicle_type='All'),
                                ~Q(owner=person.driver),
                                isConfirmed=False,
                                isComplete=False, 
                                number_of_passengers__lt=person.maximum_number_of_passenger,
                                )
        return render(request, 'uber/driver_search.html', locals())
    else:
        return render(request, 'home.html')

def driver_book(request,ride_id):
    person=DriverInfo.objects.filter(driver=request.user)[0]
    ride=Ride.objects.get(pk=ride_id)
    ride.isConfirmed=True
    ride.vehicle_type=person.vehicle_type
    ride.license_plate=person.license_plate
    ride.driver=request.user
    ride.save()
    return HttpResponse("Ride booked.")


def driver_finish(request,ride_id):
    ride=Ride.objects.get(pk=ride_id)
    ride.isComplete=True
    ride.save()
    return HttpResponse("Ride finished.")