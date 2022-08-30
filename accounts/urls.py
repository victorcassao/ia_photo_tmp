from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('newCustomer', views.create_new_customer, name="newCustomer")
]


