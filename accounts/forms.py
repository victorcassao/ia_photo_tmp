from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group
import datetime
from django.forms.fields import ChoiceField
from django.forms.widgets import Widget
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Customer

class CreateNewCustomer(forms.Form):
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={'type':'string'}), help_text="Insira seu primeiro nome")
    last_name = forms.CharField(widget=forms.TextInput(attrs={'type':'string'}), help_text="Insira seu segundo nome")
    username = forms.CharField(widget=forms.TextInput(attrs={'type':'string'}), help_text="Digite seu nome de usuário")
    email = forms.EmailField(label="Insira seu e-mail")
    company = forms.CharField(widget=forms.TextInput(attrs={'type':'string'}), help_text="Nome da empresa")
    password1 = forms.CharField(widget=forms.PasswordInput, help_text="Insira sua senha", label="Digite sua senha")
    password2 = forms.CharField(widget=forms.PasswordInput, help_text="Redigite sua senha", label="Redigite sua senha")
    
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        u = User.objects.filter(username=username)
        if u.count():
            raise ValidationError("Nome de usuário já existe.")
        return username
    
    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
        )
        
        # Crio o usuário
        user.set_password(self.cleaned_data['password2'])
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        
        customer = Customer.objects.create(company=self.cleaned_data['company'], user=user)
        
        return customer