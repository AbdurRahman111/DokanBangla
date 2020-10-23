from django.db import models

# Create your models here.


class Customer_information(models.Model):
    customer_name=models.CharField(max_length=200)
    customer_phone=models.CharField(max_length=200)
    customer_email=models.CharField(max_length=200)
    customer_password=models.CharField(max_length=200)


class Shoppkeeper_Information(models.Model):
    shoppkeeper_firstname=models.CharField(max_length=200)
    shoppkeeper_lastname=models.CharField(max_length=200)
    shopname = models.CharField(max_length=200)
    shoppkeeper_phone=models.CharField(max_length=200)
    shoppkeeper_email = models.CharField(max_length=200)

    shoppkeeper_NID=models.CharField(max_length=200)
    shop_type=models.CharField(max_length=200)
    area_delivery=models.CharField(max_length=200)
    time_delivery=models.CharField(max_length=200)
    lowest_amount=models.CharField(max_length=200)
    shoppkeeper_password=models.CharField(max_length=200)


    @staticmethod

    def shoppkeeper_login(email):
        try:
            return Shoppkeeper_Information.objects.get(shoppkeeper_email=email)
        except:
            return False
