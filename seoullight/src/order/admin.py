from django.contrib import admin
from models import Customer, Order
from order.models import testOrder
# Register your models here.
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(testOrder)