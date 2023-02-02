from . import forms
from .models import Ride
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
    return HttpResponse("Driver registration")

def selection(request):
    return HttpResponse("Select a ride")

def requestRide(request):
    model=Ride
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
                    )
            r.save()
            return render(request, 'home.html')
    return render(request, 'uber/request.html', locals())


def edit(request):
    return HttpResponse("Edit a requested ride")

def view(request):
    return HttpResponse("View ride status")

def search(request):
    return HttpResponse("Search for a ride")