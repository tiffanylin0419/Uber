from django.urls import path

from . import views
#from .views import RequestView

urlpatterns = [
    path('', views.index, name='index'),#delete
    path('registration/', views.registration, name='registration'),
    path('personal/update/', views.personUpdate, name='personUpdate'),
    path('personal/', views.personal, name='personal'),


    path('request/', views.requestRide, name='request'),
    path('myrides/', views.myrides, name='myrides'),
    path('view/<ride_id>', views.view, name='view'),
    path('update/<ride_id>', views.update, name='update'),

    path('driver_search/', views.driver_search, name='driver_search'),
    
]
