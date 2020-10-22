from django.contrib import admin
from .models import Customer_information
# Register your models here.


class Admin_customer_information(admin.ModelAdmin):
    list_display = ['customer_name','customer_phone','customer_email']

admin.site.register(Customer_information, Admin_customer_information)