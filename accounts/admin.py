from django.contrib import admin
from .models import Customer, Event, Images, Faces

# Register your models here.
admin.register(Customer)
admin.register(Event)
admin.register(Images)
admin.register(Faces)