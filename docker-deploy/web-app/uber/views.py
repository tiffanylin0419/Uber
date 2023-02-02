from . import forms
from .models import RequestRide
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
    model=RequestRide
    form = forms.RequestForm(request.POST)
    #fields = ['address']
    print("print\n")
    if form.is_valid():
        print("form is valid")
        r = RequestRide(address=form.cleaned_data['address'], pub_date=timezone.now())
        r.save()
    return render(request, 'uber/request.html', locals())

'''
class RequestView(generic.CreateView):
    model=RequestRide
    fields = ['address']
    success_url = reverse_lazy("home")
    template_name = "uber/request.html"
'''

def edit(request):
    return HttpResponse("Edit a requested ride")

def view(request):
    return HttpResponse("View ride status")

def search(request):
    return HttpResponse("Search for a ride")