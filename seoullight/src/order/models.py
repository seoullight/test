from __future__ import unicode_literals

from django.db import models
from django_enumfield import enum

class DeliveringState(enum.Enum):
    SHIPPED = 0
    WAREHOUSE_ARRIVED = 1
    SHIPPING = 2
    HOTEL_ARRIVED = 3
    FINISHED = 4

class Customer(models.Model):
    email = models.EmailField('email')
    password = models.CharField(max_length = 20)
    username = models.CharField(max_length = 20)
    gender = models.CharField(max_length = 10)
    nation = models.CharField(max_length = 30)
    age = models.IntegerField(default = 1)
    
    def __unicode__(self):
        return self.email
    
class Order(models.Model):
    customer = models.ForeignKey('Customer')
    deliveringState = enum.EnumField(DeliveringState)
    orderNumber = models.CharField(max_length = 40)
    destination = models.CharField(max_length = 100)
    baggageKind = models.CharField(max_length = 50)
    customerName = models.CharField(max_length = 50)
    quantity = models.IntegerField(default = 1)
    
    def __unicode__(self):
        return self.customer.email + '_' + self.orderNumber