from django.urls import path

from . import views
#from .views import RequestView

urlpatterns = [
    path('', views.index, name='index'),#delete
    path('registration/', views.registration, name='registration'),
    path('selection/', views.selection, name='selection'),
    path('request/', views.requestRide, name='request'),
    path('edit/', views.edit, name='edit'),
    path('view/', views.view, name='view'),
    path('search/', views.search, name='search'),

]
