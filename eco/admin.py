from django.contrib import admin
from .models import Category, Order, Product, Customer, Shopkeeper, Contact, InternshipApplication

admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Shopkeeper)
admin.site.register(Contact)

class InternshipApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'college', 'year', 'role')  # Fixed field name
    search_fields = ('name', 'email', 'college', 'role')
    list_filter = ('year', 'role')

admin.site.register(InternshipApplication, InternshipApplicationAdmin)

