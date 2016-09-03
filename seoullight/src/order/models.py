from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    eMail = models.EmailField('email')
    password = models.CharField(max_length = 20)
    gender = models.CharField(max_length = 10)
    nation = models.CharField(max_length = 30)
    age = models.IntegerField(default = 1)
    
class Order(models.Model):
    customer = models.ForeignKey('Customer')
    state = models.CharField(max_length = 20)
    destination = models.CharField(max_length = 100)
    
class testOrder(models.Model):
    email = models.EmailField('email')
    orderNumber = models.CharField(max_length = 40)
    state = models.CharField(max_length = 20)
    destination= models.CharField(max_length = 100)
    customerName = models.CharField(max_length = 50)
    baggageKind = models.CharField(max_length = 50)
    quantity = models.IntegerField(default = 1)
    