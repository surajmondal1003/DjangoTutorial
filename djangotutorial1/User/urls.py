from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from User import views

app_name='User'

urlpatterns = [

    path('user_registration',views.user_registration,name='user_registration'),
    path('user_login',views.user_login,name='user_login'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('send_email',views.send_email,name='send_email'),
    path('contact_form',views.contact_form,name='contact_form'),

]
