from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from first_app import views

app_name='first_app'

urlpatterns = [

    path('',views.index,name='index'),
    path('help',views.help,name='help'),
    path('about',views.about,name='about'),
    path('projects',views.projects,name='projects'),
    path('users',views.users,name='users'),
    path('form_page',views.form_page,name='form_page'),
    path('model_form_page',views.model_form_page,name='model_form_page'),
    path('edit_user/<id_user>',views.edit_model_form_page,name='edit_model_form_page'),
    path('delete/<id_user>', views.del_model_form_page,name='del_model_form_page'),

]
