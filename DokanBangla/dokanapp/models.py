from django.db import models

# Create your models here.


class Customer_information(models.Model):
    customer_name=models.CharField(max_length=200)
    customer_phone=models.CharField(max_length=200)
    customer_email=models.CharField(max_length=200)
    customer_password=models.CharField(max_length=200)