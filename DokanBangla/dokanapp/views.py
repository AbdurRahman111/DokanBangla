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
    firstname_shoppkeeper=request.POST.get('shoppkeeper_name_first')
    lastname_shoppkeeper=request.POST.get('shoppkeeper_name_last')
    phone_shoppkeeper=request.POST.get('shoppkeeper_phone')
    shopname_shoppkeeper=request.POST.get('shop_name')
    NID_shoppkeeper=request.POST.get('shoppkeeper_NID')
    type_shop_shoppkeeper=request.POST.get('shop_type')
    area_shoppkeeper=request.POST.get('area_delivery')
    taketime_shoppkeeper=request.POST.get('time_delivery')
    lowest_prize_shoppkeeper=request.POST.get('lowest_amount_selling')
    chack_terms_conditions_shoppkeeper=request.POST.get('chack_terms_conditions')

    print(firstname_shoppkeeper, lastname_shoppkeeper, phone_shoppkeeper, shopname_shoppkeeper, NID_shoppkeeper, type_shop_shoppkeeper,area_shoppkeeper, taketime_shoppkeeper, lowest_prize_shoppkeeper)







    return render(request, 'signup_shoppkeeper.html')

def login(request):
    return render(request, 'login.html')


def terms_conditions(request):
    return render(request, 'terms_conditions_page.html')



