from django.contrib import admin

# Register your models here.
# your_app/admin.py
from django.contrib import admin
from .models import Category,Order,Product,Customer

admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Customer)

