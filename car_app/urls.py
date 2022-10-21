from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
 
    path('',views.car_price, name='car_price'),

]