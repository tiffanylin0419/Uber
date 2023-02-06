from . import forms
from .models import Ride,DriverInfo,Sharer
from django.shortcuts import render
from django.utils import timezone
from django.db.models import F,Sum
from django.db.models import Q
from django.db.models import Count
from django.core.mail import send_mail
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
    return render(request, 'uber/registration.html', locals())


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

def personDelete(request):
    person=DriverInfo.objects.get(driver=request.user)
    rides=Ride.objects.filter(driver=person)
    for i in rides:
        i.isConfirmed=False
        i.driver=None
        i.save()
    person.delete()
    return render(request, 'home.html')

def myrides_rider(request):
    data1=Ride.objects.filter(owner=request.user ,isConfirmed=False)
    data1_2=Ride.objects.filter(id__in=Sharer.objects.filter(sharer=request.user).values_list('ride', flat=True),isConfirmed=False)
    data2=Ride.objects.filter(owner=request.user ,isConfirmed=True,isComplete=False)
    data2_2=Ride.objects.filter(id__in=Sharer.objects.filter(sharer=request.user).values_list('ride', flat=True),isConfirmed=True,isComplete=False)
    data3=Ride.objects.filter(owner=request.user ,isComplete=True)
    data3_2=Ride.objects.filter(id__in=Sharer.objects.filter(sharer=request.user).values_list('ride', flat=True),isComplete=True)
    
    return render(request, 'uber/myrides_rider.html', locals())

def myrides_driver(request):
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
    sharers = Sharer.objects.filter(ride=ride_id)
    return render(request, 'uber/view_d.html', locals())

def update(request,ride_id):
    ride=Ride.objects.get(pk=ride_id)
    form = forms.RequestUpdateForm(request.POST or None,instance=ride)
    if form.is_valid():
        form.save()
        Sharer.objects.filter(ride=ride).delete()
        return render(request, 'home.html')
    return render(request, 'uber/update.html', locals())



def search_driver(request):
    persons=DriverInfo.objects.filter(driver=request.user)
    if persons:
        person=persons[0]


        data=[]
        for i in Ride.objects.filter(Q(vehicle_type=person.vehicle_type) | Q(vehicle_type='All'),
                                    ~Q(owner=person.driver),
                                    isConfirmed=False,
                                    isComplete=False, ):
            share=Sharer.objects.filter(ride=i)
            num_sharer=sum(share.values_list('number_of_passengers', flat=True))
            isShared=Sharer.objects.filter(ride=i,sharer=request.user)

            if num_sharer+i.number_of_passengers<=person.maximum_number_of_passenger  and not isShared:
                data.append(i)
        return render(request, 'uber/search_driver.html', locals())
    else:
        return render(request, 'home.html')

def driver_book(request,ride_id):
    person=DriverInfo.objects.filter(driver=request.user)[0]
    ride=Ride.objects.get(pk=ride_id)
    ride.isConfirmed=True
    ride.driver=person
    ride.save()
    
    recipient_list = []
    recipient_list.append(ride.owner.email)
    sharers = Sharer.objects.filter(ride=ride_id)
    for person in sharers:
        recipient_list.append(person.sharer.email)
    
    message = "Thank you for waiting. Your order has been confrimed.\n"
    message += 'Driver: ' + request.user.username + '\n'
    message += 'Vehicle: ' + ride.vehicle_type + '\n'
    message += 'Address: ' + ride.address + '\n'
    message += 'Arrival time: ' + str(ride.arrival_time) + '\n'

    send_mail(
        subject='Confirmation of your order',
        message=message,
        from_email='ece568yuxin@gmail.com',
        recipient_list=recipient_list,
        fail_silently=False
    )
    return HttpResponse("You have confrimed the ride !")

def owner_delete(request,ride_id):
    ride=Ride.objects.get(pk=ride_id)
    ride.delete()
    return HttpResponse("Ride deleted.")

def driver_finish(request,ride_id):
    ride=Ride.objects.get(pk=ride_id)
    ride.isComplete=True
    ride.save()
    return HttpResponse("Ride finished.")

def driver_delete(request,ride_id):
    ride=Ride.objects.get(pk=ride_id)
    ride.isConfirmed=False
    ride.driver=None
    ride.save()
    return HttpResponse("Ride deleted.")


def search_rider(request):
    #context = {}
    if(request.method == 'POST'):
        form = forms.SharerSpecifyForm(request.POST)
        if form.is_valid():
            addr = form.cleaned_data['address']
            earliest_arrival_time =  form.cleaned_data['earliest_arrival_time']
            latest_arrival_time = form.cleaned_data['latest_arrival_time']
            number_of_passengers = form.cleaned_data['number_of_passengers']
            number_of_passengers = (int) (number_of_passengers)
            
            data=[]
            for i in Ride.objects.filter(~Q(owner=request.user), 
                                          arrival_time__range=(earliest_arrival_time, latest_arrival_time), 
                                          address = addr,
                                          isConfirmed=False,
                                          isComplete=False, 
                                          can_be_shared=True,):
                share=Sharer.objects.filter(ride=i)
                num_sharer=sum(share.values_list('number_of_passengers', flat=True))
                isShared=Sharer.objects.filter(ride=i,sharer=request.user)
                if i.number_of_passengers+num_sharer+(int)(number_of_passengers)<=8 and not isShared:
                    data.append(i) 
            
            
            return render(request, 'uber/search_result.html', locals())
    else :
        form = forms.SharerSpecifyForm()
        return render(request, 'uber/search_rider.html', locals())


def sharer_join(request, ride_id, num_passengers):
    ride = Ride.objects.get(pk=ride_id)
    s=Sharer(sharer=request.user, ride=ride, number_of_passengers=num_passengers)
    s.save()
    return HttpResponse("Join success")

def sharer_delete(request,ride_id):
    Sharer.objects.filter(ride=ride_id,sharer=request.user).delete()
    
    return HttpResponse("Ride deleted.")