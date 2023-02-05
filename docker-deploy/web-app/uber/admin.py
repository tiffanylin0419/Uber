from django.contrib import admin

# Register your models here.
from uber.models import Ride,DriverInfo, Sharer

admin.site.register(Ride)
admin.site.register(DriverInfo)
admin.site.register(Sharer)