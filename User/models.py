from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):

    #create relationship with user model
    user = models.OneToOneField(User,on_delete=models.CASCADE,)


    #additional fields
    portfolio=models.URLField(blank=True)
    profilepic=models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):

        #built in field of model User
        return self.user.username

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    phone_no=models.IntegerField(unique=True)
    subject=models.TextField()
    ip_address=models.GenericIPAddressField(null=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

