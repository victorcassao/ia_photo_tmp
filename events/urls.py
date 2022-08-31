from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('newEvent', views.EventCreateView.as_view(), name="newEvent"),
    path('', views.EventListView.as_view(), name="listEvents")
]


