from django.urls import path

from . import views
#from .views import RequestView

urlpatterns = [
    path('', views.index, name='index'),#delete
    path('registration/', views.registration, name='registration'),
    path('personal/update/', views.personUpdate, name='personUpdate'),
    path('personal/', views.personal, name='personal'),


    path('request/', views.requestRide, name='request'),
    path('myrides_rider/', views.myrides_rider, name='myrides_rider'),
    path('view/<ride_id>', views.view, name='view'),
    path('view_d/<ride_id>', views.view_d, name='view_d'),
    path('update/<ride_id>', views.update, name='update'),

    path('myrides_driver/', views.myrides_driver, name='myrides_driver'),

    path('driver_search/', views.driver_search, name='driver_search'),
    path('driver_book/<ride_id>', views.driver_book, name='driver_book'),
    path('driver_finish/<ride_id>', views.driver_finish, name='driver_finish'),
    
    
]
