from . import forms
from .models import Ride,DriverInfo
from django.shortcuts import render
from django.utils import timezone
from django.db.models import F,Sum
from django.db.models import Q
from django.db.models import Count
# Create your views here.

#add
from django.http import HttpResponse

from django.urls import reverse_lazy
from django.views import generic

def index(request):#delete
    return HttpResponse("Hello, world. You're at the polls index.")


def requestRide(request):
    form = forms.RequestForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            print("form is valid")
            r = Ride(address=form.cleaned_data['address'], 
                    date_published=timezone.now(),
                    arrival_time = form.cleaned_data['arrival_time'],
                    number_of_passengers = form.cleaned_data['number_of_passengers'],
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
    
    #kick out sharer because owner turn off can_be_shared
    data_noShare=Ride.objects.filter(can_be_shared=False)
    for i in data_noShare:
        i.sharer.clear()

    data1=Ride.objects.filter(owner=request.user ,isConfirmed=False)
    data1_2 = Ride.objects.filter(sharer=request.user ,isConfirmed=False)
    data2=Ride.objects.filter(owner=request.user ,isConfirmed=True,isComplete=False)
    data2_2=Ride.objects.filter(sharer=request.user ,isConfirmed=True,isComplete=False)
    data3=Ride.objects.filter(owner=request.user ,isComplete=True)
    data3_2=Ride.objects.filter(sharer=request.user ,isComplete=True)
    
    return render(request, 'uber/myrides_rider.html', locals())

def myrides_driver(request):

    #kick out sharer because owner turn off can_be_shared
    data_noShare=Ride.objects.filter(can_be_shared=False)
    for i in data_noShare:
        i.sharer.clear()

    persons=DriverInfo.objects.filter(driver=request.user)
    if persons:
        data1=Ride.objects.filter(driver__driver=request.user ,isComplete=False)
        data2=Ride.objects.filter(driver__driver=request.user ,isComplete=True)

        return render(request, 'uber/myrides_driver.html', locals())
    else:
        return render(request, 'home.html')
    




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



def search_driver(request):

    #kick out sharer because owner turn off can_be_shared
    data_noShare=Ride.objects.filter(can_be_shared=False)
    for i in data_noShare:
        i.sharer.clear()

    persons=DriverInfo.objects.filter(driver=request.user)
    if persons:
        person=persons[0]

        data= Ride.objects.annotate(num_sharer=Count('sharer')).filter(
                                Q(vehicle_type=person.vehicle_type) | Q(vehicle_type='All'),
                                ~Q(owner=person.driver),
                                ~Q(sharer=request.user),
                                num_sharer__lt=person.maximum_number_of_passenger+1-F('number_of_passengers'),#passenger+sharer<=max passenger
                                isConfirmed=False,
                                isComplete=False, )
        
        return render(request, 'uber/search_driver.html', locals())
    else:
        return render(request, 'home.html')

def search_rider(request):

    #kick out sharer because owner turn off can_be_shared
    data_noShare=Ride.objects.filter(can_be_shared=False)
    for i in data_noShare:
        i.sharer.clear()

    data=Ride.objects.annotate(num_sharer=Count('sharer')).filter(~Q(owner=request.user),
                            ~Q(sharer=request.user),
                            isConfirmed=False,
                            isComplete=False, 
                            can_be_shared=True,
                            num_sharer__lt=8-F('number_of_passengers'),#passenger+sharer<8
                            )
    return render(request, 'uber/search_rider.html', locals())

def driver_book(request,ride_id):
    person=DriverInfo.objects.filter(driver=request.user)[0]
    ride=Ride.objects.get(pk=ride_id)
    ride.isConfirmed=True
    ride.driver=person
    ride.save()
    return HttpResponse("Ride booked.")

def owner_delete(request,ride_id):
    ride=Ride.objects.get(pk=ride_id)
    ride.delete()
    return HttpResponse("Ride deleted.")

def driver_finish(request,ride_id):
    ride=Ride.objects.get(pk=ride_id)
    ride.isComplete=True
    ride.save()
    return HttpResponse("Ride finished.")


def sharer_specify(request):
    #context = {}
    if(request.method == 'POST'):
        form = forms.SharerSpecifyForm(request.POST)
        if form.is_valid():
            addr = form.cleaned_data['address']
            earliest_arrival_time =  form.cleaned_data['earliest_arrival_time']
            latest_arrival_time = form.cleaned_data['latest_arrival_time']
            number_of_passengers = form.cleaned_data['number_of_passengers']
            data = Ride.objects.filter(~Q(owner=request.user), 
                                       arrival_time__range=(earliest_arrival_time, latest_arrival_time), 
                                       address = addr, 
                                       # number_of_passengers
                                       isConfirmed=False,
                                       isComplete=False, 
                                       can_be_shared=True,)
            
            return render(request, 'uber/search_sharer.html', locals())
    else :
        form = forms.SharerSpecifyForm()
        return render(request, 'uber/sharer_specify.html', locals())

def sharer_join(request, ride_id):
    ride = Ride.objects.filter(pk=ride_id).first()
    ride.sharer.add(request.user)
    ride.save()
    return HttpResponse("Join success")

def sharer_delete(request,ride_id):
    ride=Ride.objects.get(pk=ride_id)
    ride.sharer.remove(request.user)
    ride.save()
    return HttpResponse("Ride deleted.")