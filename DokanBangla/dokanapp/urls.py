from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('catagory', views.catagory, name='catagory'),
    path('signup_castomer', views.signup_castomer, name='signup_castomer'),
    path('signup_shoppkeeper', views.signup_shoppkeeper, name='signup_shoppkeeper'),
    path('login', views.login, name='login'),


]
