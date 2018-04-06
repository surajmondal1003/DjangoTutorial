from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from User.models import UserProfileInfo
from django.contrib.auth.models import User
from . import forms
from User.forms import ProfileInfoForm,UserForm,ContactForm

from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.gis.geoip2 import GeoIP2
from datetime import datetime

# Create your views here.



def user_registration(request):

    registered=False

    if request.method == 'POST' :
        user_form=UserForm(data=request.POST)
        profile_form=ProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid() :

            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profilepic' in request.FILES :
                profile.profilepic=request.FILES['profilepic']

                profile.save()

                registered=True

        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=ProfileInfoForm()

    return render(request, 'User/registration.html', { 'user_form': user_form,
                                                        'profile_form': profile_form,
                                                        'registered':registered
                                                         })


def user_login(request):

    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        #print('hello')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('first_app:index'))
            else:
                return HttpResponse('Account Not Active')
        else:
            print("Someone tried to login and falied")
            print("Username:{} and password :{}".format(username,password))
            messages.error(request, 'username or password not correct')
            return render(request, 'User/login.html', {})
    else:
        return render(request,'User/login.html',{})



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('first_app:index'))



def contact_form(request):

    sent=False
    cntct_frm=ContactForm()

    if request.method == 'POST':
        cntct_frm = ContactForm(request.POST)


        if cntct_frm.is_valid():
            newcontact=cntct_frm.save(commit=False)
            #newcontact.date=datetime.now()
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

            if x_forwarded_for:
                ipaddress = x_forwarded_for.split(',')[-1].strip()
            else:
                ipaddress = request.META.get('REMOTE_ADDR')
            newcontact.ip_address=ipaddress

            newcontact.save()
            sent = True
            g = GeoIP2()
            country=g.country(ipaddress)
            print(country)

            send_email(newcontact.email,newcontact.subject)

        else:
            print("Error..")

    return render(request, 'User/send_mail.html', {'form': cntct_frm,'sent':sent})



def send_email(email,subject):
    send_mail(
        'Test',
        subject,
        'surajmondal1003@gmail.com',
        [email],
        fail_silently=False,
    )

    return HttpResponse("Mail sent Successfully")
