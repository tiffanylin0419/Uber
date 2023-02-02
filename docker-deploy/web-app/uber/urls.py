from django.urls import path

from . import views
#from .views import RequestView

urlpatterns = [
    path('', views.index, name='index'),#delete
    path('registration/', views.registration, name='registration'),
    path('myrides/', views.myrides, name='myrides'),
    path('view/<ride_id>', views.view, name='view'),
    path('update/<ride_id>', views.update, name='update'),
    path('request/', views.requestRide, name='request'),
    
    path('search/', views.search, name='search'),
    path('personal/', views.personal, name='personal'),
]
