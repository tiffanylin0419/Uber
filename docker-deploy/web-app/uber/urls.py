from django.urls import path

from . import views
#from .views import RequestView

urlpatterns = [
    path('', views.index, name='index'),#delete
    path('registration/', views.registration, name='registration'),
    path('view/', views.view, name='view'),
    path('request/', views.requestRide, name='request'),
    path('edit/', views.edit, name='edit'),
    path('myrides/', views.myrides, name='myrides'),
    path('search/', views.search, name='search'),

]
