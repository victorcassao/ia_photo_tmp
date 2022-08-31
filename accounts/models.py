from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Customer(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    company = models.CharField(max_length=255, null=True)
    isActive = models.BooleanField(default=True)
    
    def __str__(self):
        
        return self.user.get_full_name()