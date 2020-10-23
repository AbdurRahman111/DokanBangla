from django.contrib import admin
from .models import Customer_information
from .models import Shoppkeeper_Information
# Register your models here.


class Admin_customer_information(admin.ModelAdmin):
    list_display = ['customer_name','customer_phone','customer_email']


class Admin_shoppkeeper_information(admin.ModelAdmin):
    list_display = ['shoppkeeper_firstname','shoppkeeper_phone','shopname','shop_type','area_delivery','time_delivery','lowest_amount']

admin.site.register(Customer_information, Admin_customer_information)
admin.site.register(Shoppkeeper_Information, Admin_shoppkeeper_information)