from cgitb import reset
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def home(request):

    print(f"Requisição: {request.method}")


    print(f"User: {request.user.get_username()}")

    return render(request, 'home.html', {})


