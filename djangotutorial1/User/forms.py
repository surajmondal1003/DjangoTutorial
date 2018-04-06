from django import forms
from django.contrib.auth.models import User
from User.models import UserProfileInfo,Contact

class UserForm(forms.ModelForm):
    username = forms.CharField(label='User Name',
                           widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'on'}))
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'autocomplete': 'on'}))
    password=forms.CharField(label='Password',
                            widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'on'}))

    class Meta:
        model=User
        fields=('username','email','password')

class ProfileInfoForm(forms.ModelForm):

    portfolio=forms.URLField(required=False,label='Portfolio',
                        widget=forms.URLInput(attrs={'class': 'form-control', 'autocomplete': 'on'}))
    profilepic=forms.ImageField(required=False,label='Profile Picture')

    class Meta:
        model=UserProfileInfo
        fields=('portfolio','profilepic')

class ContactForm(forms.ModelForm):

    class Meta:
        model=Contact
        exclude=['ip_address','date']