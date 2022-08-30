from cgitb import reset
from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import CreateNewCustomer
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

# Create your views here.
def home(request):

    print(f"Requisição: {request.method}")


    print(f"User: {request.user.get_username()}")

    return render(request, 'home.html', {})


def create_new_customer(request):
    
    if request.method == 'POST':
        form = CreateNewCustomer(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('login'))
    else:
        p_form = CreateNewCustomer()
        
    return render(request, 'customer/createNewCustomer.html', {'form': p_form})
        

