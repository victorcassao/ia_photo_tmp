from django.contrib import admin
from .models import Customer, Event, Image, Face

# Register your models here.
admin.site.register(Customer)
admin.site.register(Event)
admin.site.register(Image)
admin.site.register(Face)