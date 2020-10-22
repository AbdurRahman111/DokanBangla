from django.shortcuts import render , redirect
from .models import Customer_information
from django.contrib.auth.hashers import check_password, make_password


# Create your views here.


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def catagory(request):
    return render(request, 'catagory.html')

def signup_castomer(request):

    if request.method=="GET":
        return render(request, 'signup_castomer.html')

    else:


        cname=request.POST.get('cus_name')
        cphone=request.POST.get('cus_phone')
        cemail=request.POST.get('cus_email')
        cpassword1=request.POST.get('cus_password')
        cpassword=make_password(cpassword1)

        custo_sign_save_data=Customer_information(

            customer_name=cname,
            customer_phone = cphone,
            customer_email = cemail,
            customer_password =cpassword

        )

        custo_sign_save_data.save()

        return render(request, 'index.html')

def signup_shoppkeeper(request):
    return render(request, 'signup_shoppkeeper.html')

def login(request):
    return render(request, 'login.html')



