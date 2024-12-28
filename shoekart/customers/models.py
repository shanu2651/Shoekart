from django.db import models
from django.contrib.auth.models import User

# model for customer.
class Customer(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'live'),(DELETE,'Delete'))
    name=models.CharField(max_length=50)
    address=models.TextField()
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='customer_profile')
    phone=models.CharField(max_length=10) 
    priority=models.IntegerField(default=0)
    delete_status=models.ImageField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

def __str__() -> str:
    return self.title
