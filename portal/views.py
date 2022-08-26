from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Customer
from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    
    return HttpResponse("Hello, world")

# Customer
class CustomerListView(generic.ListView):
    model = Customer
    fields = '__all__'

class CustomerCreate(generic.CreateView):
    model = Customer
    fields = "__all__"

    def get_success_url(self):
        return reverse('listar_clientes')
    