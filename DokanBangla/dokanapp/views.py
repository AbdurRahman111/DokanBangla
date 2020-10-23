from django.shortcuts import render , redirect
from .models import Customer_information
from django.contrib.auth.hashers import check_password, make_password
from .models import Shoppkeeper_Information
from django.http import HttpResponse

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

    if request.method=="GET":
        return render(request, 'signup_shoppkeeper.html')

    else:


        firstname_shoppkeeper = request.POST.get('shoppkeeper_name_first')
        lastname_shoppkeeper = request.POST.get('shoppkeeper_name_last')
        shopname_shoppkeeper = request.POST.get('shop_name')
        phone_shoppkeeper = request.POST.get('shoppkeeper_phone')
        shoppkeeper_email = request.POST.get('shoppkeeper_email')
        NID_shoppkeeper = request.POST.get('shoppkeeper_NID')
        type_shop_shoppkeeper = request.POST.get('shop_type')
        area_shoppkeeper = request.POST.get('area_delivery')
        taketime_shoppkeeper = request.POST.get('time_delivery')
        lowest_prize_shoppkeeper = request.POST.get('lowest_amount_selling')
        shoppkeeper_password1 = request.POST.get('shoppkeeper_password')
        shoppkeeper_password = make_password(shoppkeeper_password1)


        chack_terms_conditions_shoppkeeper = request.POST.get('chack_terms_conditions')

        if chack_terms_conditions_shoppkeeper == 'on':

            get_data_shoppkeeper=Shoppkeeper_Information(

                shoppkeeper_firstname=firstname_shoppkeeper,
                shoppkeeper_lastname = lastname_shoppkeeper,
                shopname=shopname_shoppkeeper,
                shoppkeeper_phone = phone_shoppkeeper,
                shoppkeeper_email=shoppkeeper_email,
                shoppkeeper_NID = NID_shoppkeeper,
                shop_type = type_shop_shoppkeeper,
                area_delivery = area_shoppkeeper,
                time_delivery = taketime_shoppkeeper,
                lowest_amount = lowest_prize_shoppkeeper,
                shoppkeeper_password = shoppkeeper_password



            )
            get_data_shoppkeeper.save()



        else:
            return HttpResponse('<h1>you haue to chack to our terms and conditions!!!<h1>')


        return render(request, 'signup_shoppkeeper.html')

def customer_login(request):



    return render(request, 'customer_login.html')



def shoppkeeper_login(request):
    if request.method=="GET":
        return render(request, 'shoppkeeper_login.html')

    else:


        shoppkeeper_login_email = request.POST.get('shoppkeeper_login_email')
        shoppkeeper_login_password = request.POST.get('shoppkeeper_login_password')

        matching_email=Shoppkeeper_Information.shoppkeeper_login(shoppkeeper_login_email)
        if matching_email:
            matching_pass= check_password(shoppkeeper_login_password, matching_email.shoppkeeper_password)
            if matching_pass:
                return HttpResponse('<h1>you are loged in !!!!</h1>')
            else:
                return HttpResponse('<h1>incorrect password</h1>')

        else:
            # return HttpResponse('<h1>iccorrect email</h1>')
            return render(request, 'alart.html')

        return render(request, 'shoppkeeper_login.html')


def terms_conditions(request):
    return render(request, 'terms_conditions_page.html')


def profile(request):
    return render(request, 'profile.html')



