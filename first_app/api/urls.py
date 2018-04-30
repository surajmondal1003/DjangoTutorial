from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from . views import  (
    UsersListAPIView,
    UsersDetailAPIView,
    UsersUpdateAPIView,
    UsersDeleteAPIView,
    UsersCreateAPIView
    )

app_name='first_app'

urlpatterns = [

    # path('',views.index,name='index'),
    # path('help',views.help,name='help'),
    # path('about',views.about,name='about'),
    # path('projects',views.projects,name='projects'),
    path('users',UsersListAPIView.as_view(),name='users'),
    path('users/<pk>',UsersDetailAPIView.as_view(),name='users_detail'),
    # path('form_page',views.form_page,name='form_page'),
     path('create_user',UsersCreateAPIView.as_view(),name='create_user'),
     path('edit_user/<pk>',UsersUpdateAPIView.as_view(),name='edit_model_form_page'),
     path('delete/<pk>', UsersDeleteAPIView.as_view(),name='del_model_form_page'),

]
