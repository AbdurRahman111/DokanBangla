from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('catagory', views.catagory, name='catagory'),
    path('signup_castomer', views.signup_castomer, name='signup_castomer'),
    path('signup_shoppkeeper', views.signup_shoppkeeper, name='signup_shoppkeeper'),
    path('customer_login', views.customer_login, name='customer_login'),
    path('shoppkeeper_login', views.shoppkeeper_login, name='shoppkeeper_login'),
    path('terms_conditions', views.terms_conditions, name='terms_conditions'),
    path('profile', views.profile, name='profile'),


]
