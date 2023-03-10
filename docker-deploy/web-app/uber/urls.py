from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),#delete
    path('registration/', views.registration, name='registration'),
    
    path('personal/', views.personal, name='personal'),
    path('personal/update/', views.personUpdate, name='personUpdate'),
    path('personal/delete/', views.personDelete, name='personDelete'),


    path('request/', views.requestRide, name='request'),
    path('myrides_rider/', views.myrides_rider, name='myrides_rider'),
    path('view/<ride_id>', views.view, name='view'),
    path('view_d/<ride_id>', views.view_d, name='view_d'),
    path('update/<ride_id>', views.update, name='update'),

    path('myrides_driver/', views.myrides_driver, name='myrides_driver'),

    path('search_driver/', views.search_driver, name='search_driver'),
    path('search_rider/', views.search_rider, name='search_rider'),

    
    path('owner_delete/<ride_id>', views.owner_delete, name='owner_delete'),

    path('driver_book/<ride_id>', views.driver_book, name='driver_book'),
    path('driver_finish/<ride_id>', views.driver_finish, name='driver_finish'),
    path('driver_delete/<ride_id>', views.driver_delete, name='driver_delete'),

    #path('sharer_specify/', views.sharer_specify, name='sharer_specify'),
    #also add in home.html

    #path('search_sharer/', views.search_sharer, name='search_sharer'),
    
    path('sharer_join/<ride_id>/<num_passengers>', views.sharer_join, name='sharer_join'),
    path('sharer_delete/<ride_id>', views.sharer_delete, name='sharer_delete'),
    
]
